# SQLite compatibility fix (only needed for certain deployment environments)
try:
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    # pysqlite3 not available (e.g., on Windows) - use standard sqlite3
    pass

import streamlit as st
import os
from datetime import datetime
import json
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

import gspread
from google.oauth2.service_account import Credentials
import cohere
import chromadb
from google import genai
from google.genai import types

# Import UI styles and constants
from styles import (
    apply_custom_styles, 
    render_welcome_message, 
    render_sidebar_footer,
    EXAMPLE_QUESTIONS,
    PAGE_CONFIG,
    AVATAR_USER,
    AVATAR_ASSISTANT,
    UI_TEXT
)

# =============================================================================
# CONFIGURATION
# =============================================================================

GSHEET_NAME = "NUU Analytics"
GSHEET_TAB = "Sheet1"

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# =============================================================================
# GOOGLE SHEETS LOGGING
# =============================================================================

def get_gsheet_client_from_st_secrets():
    """Initialize Google Sheets client from Streamlit secrets."""
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    )
    gc = gspread.authorize(creds)
    return gc

def log_to_gsheet(question, answer, timestamp_sheet):
    """Log conversation to Google Sheets."""
    try:
        gc = get_gsheet_client_from_st_secrets()
        sh = gc.open(GSHEET_NAME)
        ws = sh.worksheet(GSHEET_TAB)
        ws.append_row([timestamp_sheet, question, answer])
    except Exception as e:
        st.warning(f"Could not log to Google Sheets: {e}")

# =============================================================================
# API CLIENTS INITIALIZATION
# =============================================================================

if not COHERE_API_KEY or not GEMINI_API_KEY:
    st.error("COHERE_API_KEY or GEMINI_API_KEY is missing")
    st.stop()

co = cohere.Client(COHERE_API_KEY)
genai_client = genai.Client(api_key=GEMINI_API_KEY)
client = chromadb.Client()
collection = client.get_or_create_collection(name="nuu-assistant", embedding_function=None)

# =============================================================================
# RAG FUNCTIONS
# =============================================================================

def retrieve_context(question, collection, top_k=2):
    """Retrieve relevant context from vector database."""
    qr = co.embed(
        texts=[question],
        model="embed-english-v3.0",
        input_type="search_query"
    )
    emb = qr.embeddings[0]
    results = collection.query(query_embeddings=[emb], n_results=top_k)
    return "\n".join(results["documents"][0])

def get_prompt_plain(context: str, question: str) -> str:
    """Generate prompt for LLM."""
    return f"""
<<START>>
You are a helpful assistant for New Uzbekistan University (NUU). Using the context below, answer within 300 tokens.
Create interactive, well-structured answers using bullet points, bold text, and proper formatting to make the information concise, answer-oriented, clear and easy to read.

When the context doesn't provide what the user asked, don't mention it. Instead, politely say you don't know.

Your important job is to first identify if the question is related to your role, which is New Uzbekistan University related information. If the question isn't related to it, for example users may say "thank you" or "how are you?", then don't provide a link because they aren't valid questions. ONLY provide a link when the question is genuinely about NUU.

In the context text, there will always be a link where this info is taken from. At the end of your response, tell the user they can visit this link for official information, then provide the link.

At the end of your response, don't forget to say polite words like "Have a nice day!", "Have a wonderful day!", "Have an awesome day!", "Stay awesome!", "Make it a great day!", "Go make some magic happen!", "Here's to a fantastic day ahead!", "May your day be filled with good things!", or "Hope something wonderful happens to you today!". Adjust them based on the question context.

Context:
"{context}"

Question: {question}

Answer:
<<END>>"""

def generate_agent_answer(context: str, question: str) -> str:
    """Generate answer using Gemini."""
    prompt = get_prompt_plain(context, question)
    response = genai_client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.01,
            top_p=0.8,
            stop_sequences=["<<END>>", "<<START>>"]
        )
    )
    return response.text.strip()

def rag_answer(question: str, collection) -> str:
    """Complete RAG pipeline: retrieve + generate."""
    if not question.strip():
        return "Please enter a question about New Uzbekistan University."
    context = retrieve_context(question, collection, top_k=2)
    return generate_agent_answer(context, question)

# =============================================================================
# DATA INITIALIZATION
# =============================================================================

@st.cache_data
def initialize_collection():
    """Load documents into vector database."""
    total_docs = collection.count() if hasattr(collection, 'count') else len(collection.get()['documents'])
    if total_docs == 0:
        content_chunks = []
        for i in range(1, 4):
            folder_path = os.path.join(os.getcwd(), "docs", f"p0000{i}")
            if not os.path.exists(folder_path):
                continue
            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"):
                    with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                        content = f.read()
                        content_chunks.append(f"search_document: {content}")
        
        if content_chunks:
            response = co.embed(
                texts=content_chunks,
                model="embed-english-v3.0",
                input_type="search_document"
            )
            embeddings = response.embeddings
            collection.add(
                ids=[str(i) for i in range(len(content_chunks))],
                documents=content_chunks,
                embeddings=embeddings
            )
    return True

# =============================================================================
# STREAMLIT UI - PAGE CONFIG
# =============================================================================

st.set_page_config(**PAGE_CONFIG)

# Apply custom styles
apply_custom_styles()

# =============================================================================
# SESSION STATE INITIALIZATION
# =============================================================================

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'collection_initialized' not in st.session_state:
    st.session_state.collection_initialized = False

# Initialize collection
if not st.session_state.collection_initialized:
    with st.spinner(UI_TEXT["loading_message"]):
        initialize_collection()
        st.session_state.collection_initialized = True

# =============================================================================
# SIDEBAR
# =============================================================================

with st.sidebar:
    st.title(UI_TEXT["sidebar_title"])
    st.markdown(UI_TEXT["sidebar_description"])
    st.divider()
    
    # Example Questions
    st.subheader(UI_TEXT["example_questions_header"])
    for i, example in enumerate(EXAMPLE_QUESTIONS):
        if st.button(example, key=f"example_{i}", use_container_width=True):
            timestamp = datetime.now(ZoneInfo("Asia/Tashkent")).strftime("%H:%M")
            st.session_state.chat_history.append({
                "role": "user",
                "content": example,
                "timestamp": timestamp
            })
            with st.spinner(UI_TEXT["thinking_message"]):
                answer = rag_answer(example, collection)
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": answer,
                    "timestamp": timestamp
                })
                try:
                    log_to_gsheet(example, answer, timestamp)
                except Exception as e:
                    st.warning(f"Could not log to Google Sheets: {e}")
            st.rerun()
    
    st.divider()
    
    # Chat Management
    st.subheader(UI_TEXT["chat_management_header"])
    
    if st.session_state.chat_history:
        user_messages = len([msg for msg in st.session_state.chat_history if msg["role"] == "user"])
        st.info(f"{UI_TEXT['questions_asked_label']}: {user_messages}")
    
    if st.button(UI_TEXT["clear_history_button"], use_container_width=True):
        st.session_state.chat_history = []
        st.success(UI_TEXT["clear_success"])
        st.rerun()
    
    if st.session_state.chat_history:
        chat_data = json.dumps(st.session_state.chat_history, indent=2, ensure_ascii=False)
        st.download_button(
            label=UI_TEXT["export_history_button"],
            data=chat_data,
            file_name=f"nuu_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True
        )
    
    st.divider()
    
    # Service Info
    st.subheader(UI_TEXT["service_info_header"])
    try:
        doc_count = collection.count() if hasattr(collection, 'count') else len(collection.get()['documents'])
        st.metric(UI_TEXT["questions_asked_label"], "500+")
    except:
        st.metric("Documents Loaded", "Unknown")
    
    st.success(UI_TEXT["thank_you_message"])
    st.markdown("---")
    render_sidebar_footer()

# =============================================================================
# MAIN CHAT INTERFACE
# =============================================================================

st.title(UI_TEXT["main_title"])
st.markdown(UI_TEXT["main_description"])

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            with st.chat_message("user", avatar=AVATAR_USER):
                st.write(f"**You** - *{message['timestamp']}*")
                st.write(message["content"])
        else:
            with st.chat_message("assistant", avatar=AVATAR_ASSISTANT):
                st.write(f"**NewUU Assistant** - *{message['timestamp']}*")
                st.markdown(message["content"])

# Chat input
if prompt := st.chat_input(UI_TEXT["chat_input_placeholder"], key="main_input"):
    timestamp = datetime.now(ZoneInfo("Asia/Tashkent")).strftime("%H:%M")
    
    # Add user message
    st.session_state.chat_history.append({
        "role": "user",
        "content": prompt,
        "timestamp": timestamp
    })
    
    # Display user message
    with st.chat_message("user", avatar=AVATAR_USER):
        st.write(f"**You** - *{timestamp}*")
        st.write(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant", avatar=AVATAR_ASSISTANT):
        st.write(f"**NewUU Assistant** - *{timestamp}*")
        with st.spinner(UI_TEXT["searching_message"]):
            response = rag_answer(prompt, collection)
            st.markdown(response)
    
    # Add assistant message to history
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": response,
        "timestamp": timestamp
    })
    
    # Log to Google Sheets
    try:
        timestamp_sheet = datetime.now(ZoneInfo("Asia/Tashkent")).strftime("%Y-%m-%d %H:%M") 
        log_to_gsheet(prompt, response, timestamp_sheet)
    except Exception as e:
        st.warning(f"Could not log to Google Sheets: {e}")

# Display welcome message if no chat history
if not st.session_state.chat_history:
    render_welcome_message()