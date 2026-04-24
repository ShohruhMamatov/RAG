

# Custom CSS styles for the application
CUSTOM_CSS = """
<style>
    button[data-testid="collapsedControl"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        position: fixed !important;
        top: 1rem !important;
        left: 1rem !important;
        z-index: 999999 !important;
        background-color: #ffffff !important;
        border: 1px solid #ccc !important;
        border-radius: 4px !important;
        padding: 8px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
    }
    
    @media (prefers-color-scheme: dark) {
        button[data-testid="collapsedControl"] {
            background-color: #262730 !important;
            border: 1px solid #464852 !important;
            color: #fafafa !important;
        }
    }
    
    [data-theme="dark"] button[data-testid="collapsedControl"] {
        background-color: #262730 !important;
        border: 1px solid #464852 !important;
        color: #fafafa !important;
    }

    .stChatMessage {
        background-color: #f8f9fa !important;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
    }

    .stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 1px solid #ddd !important;
        background-color: #ffffff !important;
        color: #333 !important;
        padding: 10px 15px;
        text-align: left;
        font-size: 14px;
        transition: all 0.3s ease;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    .stButton > button:hover {
        background-color: #f0f2f6 !important;
        border-color: #0066cc !important;
        transform: translateY(-1px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .stMetric {
        background-color: #f8f9fa !important;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #0066cc;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    h1 {
        color: #0066cc !important;
        font-weight: 600;
        border-bottom: 2px solid #e8f4f8;
        padding-bottom: 10px;
    }

    .stDownloadButton > button {
        background-color: #28a745 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px;
        padding: 10px 15px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        background-color: #218838 !important;
        transform: translateY(-1px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    div[data-testid="stButton"] button[kind="secondary"] {
        background-color: #dc3545 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    div[data-testid="stButton"] button[kind="secondary"]:hover {
        background-color: #c82333 !important;
        transform: translateY(-1px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    @media (prefers-color-scheme: dark) {
        .stChatMessage {
            background-color: #262730 !important;
            border: 1px solid #464852 !important;
            box-shadow: 0 1px 3px rgba(255,255,255,0.1) !important;
            color: #fafafa !important;
        }
        
        .stChatMessage p, .stChatMessage span, .stChatMessage div,
        .stChatMessage strong, .stChatMessage em {
            color: #fafafa !important;
        }
        
        .stButton > button {
            background-color: #262730 !important;
            color: #fafafa !important;
            border: 1px solid #464852 !important;
            box-shadow: 0 1px 2px rgba(255,255,255,0.05) !important;
        }
        
        .stButton > button:hover {
            background-color: #1e1e1e !important;
            border-color: #4dabf7 !important;
            color: #fafafa !important;
            box-shadow: 0 2px 4px rgba(255,255,255,0.1) !important;
        }
        
        .stMetric {
            background-color: #262730 !important;
            border-left: 4px solid #4dabf7 !important;
            color: #fafafa !important;
            box-shadow: 0 1px 3px rgba(255,255,255,0.1) !important;
        }
        
        .stMetric label, .stMetric [data-testid="metric-value"] {
            color: #fafafa !important;
        }
        
        h1 {
            color: #4dabf7 !important;
            border-bottom: 2px solid #464852 !important;
        }
        
        h2, h3, h4, h5, h6 {
            color: #fafafa !important;
        }
        
        .stMarkdown, .stMarkdown p, .stMarkdown span, .stMarkdown div {
            color: #fafafa !important;
        }
        
        .stSidebar p, .stSidebar span, .stSidebar div, .stSidebar h1, .stSidebar h2, .stSidebar h3 {
            color: #fafafa !important;
        }
        
        .stSuccess, .stInfo, .stWarning {
            background-color: #262730 !important;
            color: #fafafa !important;
            box-shadow: 0 1px 3px rgba(255,255,255,0.1) !important;
        }
        
        .stTextInput input, .stChatInput input, .stSelectbox select {
            background-color: #262730 !important;
            color: #fafafa !important;
            border: 1px solid #464852 !important;
        }
        
        .stDownloadButton > button {
            background-color: #51cf66 !important;
            color: #1e1e1e !important;
        }
        
        .stDownloadButton > button:hover {
            background-color: #40c057 !important;
        }
        
        div[data-testid="stButton"] button[kind="secondary"] {
            background-color: #ff6b6b !important;
            color: white !important;
        }
        
        div[data-testid="stButton"] button[kind="secondary"]:hover {
            background-color: #ff5252 !important;
        }
        
        hr {
            background: linear-gradient(to right, transparent, #4dabf7, transparent) !important;
        }
        
        .stChatInputContainer {
            border-top: 1px solid #464852 !important;
        }
        
        ::-webkit-scrollbar-track {
            background: #262730 !important;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #464852 !important;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #5a5a5a !important;
        }
    }

    [data-theme="dark"] .stChatMessage {
        background-color: #262730 !important;
        border: 1px solid #464852 !important;
        color: #fafafa !important;
        box-shadow: 0 1px 3px rgba(255,255,255,0.1) !important;
    }
    
    [data-theme="dark"] .stChatMessage p, 
    [data-theme="dark"] .stChatMessage span, 
    [data-theme="dark"] .stChatMessage div,
    [data-theme="dark"] .stChatMessage strong, 
    [data-theme="dark"] .stChatMessage em {
        color: #fafafa !important;
    }
    
    [data-theme="dark"] .stButton > button {
        background-color: #262730 !important;
        color: #fafafa !important;
        border: 1px solid #464852 !important;
        box-shadow: 0 1px 2px rgba(255,255,255,0.05) !important;
    }
    
    [data-theme="dark"] .stButton > button:hover {
        background-color: #1e1e1e !important;
        border-color: #4dabf7 !important;
        color: #fafafa !important;
        box-shadow: 0 2px 4px rgba(255,255,255,0.1) !important;
    }
    
    [data-theme="dark"] .stMetric {
        background-color: #262730 !important;
        border-left: 4px solid #4dabf7 !important;
        color: #fafafa !important;
        box-shadow: 0 1px 3px rgba(255,255,255,0.1) !important;
    }
    
    [data-theme="dark"] h1 {
        color: #4dabf7 !important;
        border-bottom: 2px solid #464852 !important;
    }
    
    [data-theme="dark"] h2, [data-theme="dark"] h3, [data-theme="dark"] h4, [data-theme="dark"] h5, [data-theme="dark"] h6 {
        color: #fafafa !important;
    }
    
    [data-theme="dark"] .stMarkdown, 
    [data-theme="dark"] .stMarkdown p, 
    [data-theme="dark"] .stMarkdown span, 
    [data-theme="dark"] .stMarkdown div {
        color: #fafafa !important;
    }
    
    [data-theme="dark"] .stSidebar p, 
    [data-theme="dark"] .stSidebar span, 
    [data-theme="dark"] .stSidebar div, 
    [data-theme="dark"] .stSidebar h1, 
    [data-theme="dark"] .stSidebar h2, 
    [data-theme="dark"] .stSidebar h3 {
        color: #fafafa !important;
    }

    .stSpinner {
        color: #0066cc;
    }
    
    @media (prefers-color-scheme: dark) {
        .stSpinner {
            color: #4dabf7 !important;
        }
    }
    
    [data-theme="dark"] .stSpinner {
        color: #4dabf7 !important;
    }
    
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #0066cc, transparent);
        margin: 20px 0;
    }
    
    .stChatInputContainer {
        border-top: 1px solid #e0e0e0;
        padding-top: 15px;
        margin-top: 20px;
    }
    
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #c1c1c1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #a8a8a8;
    }

    header[data-testid="stHeader"] > div:first-child {
        display: none;
    }

    footer {
        display: none;
    }
</style>
"""

# Welcome message markdown
WELCOME_MESSAGE = """
### Welcome to NUU Assistant! 🎓

Get specific and accurate information about New Uzbekistan University. Ask any questions about:

- 📚 Programs, courses, and academic requirements
- 🎯 Admission process and application procedures
- 💰 Scholarships, tuition fees, and financial aid
- 👥 Faculty, departments, and facilities
- 🏠 Campus life, dormitories, and student activities
- 📜 Graduation requirements and degree programs
- 🌍 International students and exchange programs

Click on example questions in the sidebar to get started!
"""

# Footer markdown for sidebar
SIDEBAR_FOOTER = """
<div style='text-align: center; color: #666; font-size: 12px;'>
    <p>New Uzbekistan University<br>
    Built with Streamlit</p>
</div>
"""

# Example questions for sidebar
EXAMPLE_QUESTIONS = [
    "How do I apply to New Uzbekistan University?",
    "Tell me about admission requirements",
    "I have an SAT score of 1300. Do I still need to take the entrance exam?",
    "What subjects are on the entrance exam for Engineering?",
    "Can I transfer from another university to NewUU?"
]

# UI configuration constants
PAGE_CONFIG = {
    "page_title": "NUU Assistant - New Uzbekistan University Info",
    "page_icon": "🎓",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Chat avatars
AVATAR_USER = "👤"
AVATAR_ASSISTANT = "🎓"

# UI text constants
UI_TEXT = {
    "sidebar_title": "🎓 NewUU Assistant",
    "sidebar_description": "Get answers to your questions about New Uzbekistan University.",
    "main_title": "🎓 New Uzbekistan University Info Assistant",
    "main_description": "Ask me anything about New Uzbekistan University!",
    "chat_input_placeholder": "e.g. What are the tuition fees at NUU?",
    "loading_message": "Loading knowledge base...",
    "thinking_message": "Thinking...",
    "searching_message": "Searching knowledge base...",
    "clear_history_button": "Clear Chat History",
    "export_history_button": "Export Chat History",
    "clear_success": "Chat history cleared!",
    "example_questions_header": "Example Questions",
    "chat_management_header": "Chat Management",
    "service_info_header": "Service Info",
    "questions_asked_label": "Questions asked",
    "thank_you_message": "Thank You!"
}


def apply_custom_styles():
    """
    Apply custom CSS styles to the Streamlit app.
    Call this function once in your main app.
    """
    import streamlit as st
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def render_welcome_message():
    """
    Render the welcome message when no chat history exists.
    """
    import streamlit as st
    st.markdown(WELCOME_MESSAGE)


def render_sidebar_footer():
    """
    Render the footer in the sidebar.
    """
    import streamlit as st
    st.markdown(SIDEBAR_FOOTER, unsafe_allow_html=True)