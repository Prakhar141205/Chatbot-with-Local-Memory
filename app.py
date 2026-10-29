
"""
Note: 
    The user interface of this mini-project was developed with the assistance of AI tools using Streamlit.
"""
import streamlit as st
from datetime import datetime

import config
import llm_client


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Memora AI | Chat with Memory",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    /* Import fonts */
    @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
    );

    /* Global styles */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 10% 0%,
                rgba(94, 92, 230, 0.12),
                transparent 35%
            ),
            #0b0d17;
        color: #f1f5f9;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #101321;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }

    /* Main container */
    .block-container {
        max-width: 1050px;
        padding-top: 2rem;
        padding-bottom: 7rem;
    }

    /* Brand */
    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 1.5rem;
    }

    .brand-icon {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        font-size: 25px;
        background: linear-gradient(135deg, #7c5cff, #4f46e5);
        box-shadow: 0 6px 25px rgba(99, 102, 241, 0.25);
    }

    .brand-name {
        font-size: 23px;
        font-weight: 800;
        letter-spacing: -0.8px;
        color: #ffffff;
    }

    .brand-subtitle {
        font-size: 11px;
        color: #9299b2;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    /* Header */
    .hero {
        padding: 30px;
        border: 1px solid rgba(255,255,255,0.09);
        border-radius: 24px;
        background: linear-gradient(
            120deg,
            rgba(124, 92, 255, 0.17),
            rgba(37, 99, 235, 0.07),
            rgba(16, 19, 33, 0.75)
        );
        margin-bottom: 25px;
    }

    .hero-badge {
        display: inline-block;
        padding: 6px 11px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        color: #c4b5fd;
        background: rgba(124, 92, 255, 0.16);
        border: 1px solid rgba(167, 139, 250, 0.22);
        margin-bottom: 15px;
    }

    .hero h1 {
        font-size: clamp(28px, 4vw, 42px);
        line-height: 1.2;
        letter-spacing: -1.5px;
        margin: 0 0 12px 0;
        color: #ffffff;
    }

    .hero h1 span {
        background: linear-gradient(90deg, #a78bfa, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero p {
        font-size: 14px;
        line-height: 1.8;
        max-width: 650px;
        color: #a5acc4;
        margin: 0;
    }

    /* Status cards */
    .status-card {
        padding: 16px;
        min-height: 88px;
        border-radius: 16px;
        background: rgba(22, 26, 43, 0.85);
        border: 1px solid rgba(255,255,255,0.07);
        margin-bottom: 10px;
    }

    .status-label {
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #9299b2;
        margin-bottom: 9px;
    }

    .status-value {
        font-size: 15px;
        font-weight: 700;
        color: #f1f5f9;
    }

    .status-dot {
        display: inline-block;
        height: 8px;
        width: 8px;
        border-radius: 50%;
        background: #34d399;
        margin-right: 7px;
    }

    /* Sidebar sections */
    .sidebar-label {
        color: #9299b2;
        font-size: 11px;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 1.5px;
        margin-top: 25px;
        margin-bottom: 12px;
    }

    .feature-item {
        padding: 12px;
        margin: 8px 0;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.06);
        background: rgba(255,255,255,0.025);
        font-size: 13px;
        color: #cbd5e1;
    }

    /* Chat messages */
    div[data-testid="stChatMessage"] {
        padding: 16px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.06);
        background: rgba(20, 24, 40, 0.80);
        margin-bottom: 14px;
    }

    div[data-testid="stChatMessage"] p {
        font-size: 14px;
        line-height: 1.8;
    }

    /* Input */
    div[data-testid="stChatInput"] {
        border-radius: 18px;
        border: 1px solid rgba(139, 92, 246, 0.4);
        background: #15182a;
        box-shadow: 0 8px 35px rgba(0,0,0,0.2);
    }

    div[data-testid="stChatInput"] textarea {
        color: #ffffff;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 10px 14px;
        font-weight: 600;
        border: 1px solid rgba(255,255,255,0.1);
        background: #191d31;
        color: #f1f5f9;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #8b5cf6;
        color: #c4b5fd;
        background: #22203e;
    }

    /* Welcome screen */
    .welcome {
        text-align: center;
        padding: 45px 20px 25px;
    }

    .welcome-icon {
        width: 78px;
        height: 78px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: auto auto 20px;
        border-radius: 25px;
        font-size: 38px;
        background: linear-gradient(
            135deg,
            rgba(124,92,255,0.25),
            rgba(59,130,246,0.18)
        );
        border: 1px solid rgba(167,139,250,0.2);
    }

    .welcome h2 {
        color: #ffffff;
        font-size: 25px;
        letter-spacing: -0.6px;
    }

    .welcome p {
        font-size: 14px;
        line-height: 1.8;
        color: #9299b2;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #747c95;
        font-size: 11px;
        margin-top: 40px;
        padding: 15px;
        border-top: 1px solid rgba(255,255,255,0.06);
    }

    /* Mobile responsiveness */
    @media (max-width: 640px) {
        .block-container {
            padding: 1rem 1rem 6rem;
        }

        .hero {
            padding: 22px;
        }

        .hero h1 {
            letter-spacing: -0.7px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


def build_messages(history: list[dict], user_input: str) -> list[dict]:
    """Build messages with system instructions and conversation history."""

    messages = [
        {
            "role": "system",
            "content": config.SYSTEM_PROMPT
        }
    ]

    messages.extend(
        {
            "role": message["role"],
            "content": message["content"]
        }
        for message in history
        if message["role"] in ("user", "assistant")
    )

    messages.append({
        "role": "user",
        "content": user_input
    })

    return messages




if "messages" not in st.session_state:
    st.session_state.messages = []

if "message_times" not in st.session_state:
    st.session_state.message_times = []



with st.sidebar:

    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">🤖</div>
            <div>
                <div class="brand-name">Memora AI</div>
                <div class="brand-subtitle">Intelligent Chat</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        '<div class="sidebar-label">Workspace</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="feature-item">💬 &nbsp; AI Conversation</div>
        <div class="feature-item">🧠 &nbsp; Conversation Memory</div>
        <div class="feature-item">⚡ &nbsp; Multi-Provider Support</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-label">Model Configuration</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="status-card">
            <div class="status-label">Selected Provider</div>
            <div class="status-value">
                <span class="status-dot"></span>
                {config.LLM_PROVIDER}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="status-card">
            <div class="status-label">Conversation Messages</div>
            <div class="status-value">
                {len(st.session_state.messages)}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-label">Actions</div>',
        unsafe_allow_html=True
    )

    if st.button("🗑️  Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.message_times = []
        st.rerun()

    st.markdown("---")

    st.caption("Built with Streamlit & LangChain")
    st.caption("Memora AI · Mini Project")


# --------------------------------------------------
# CONFIGURATION VALIDATION
# --------------------------------------------------

configuration_error = config.get_configuration_error()

if configuration_error:
    st.error(f"⚙️ Configuration problem: {configuration_error}")
    st.info(
        "Check your .env file and ensure the selected provider "
        "has the required API key and model configuration."
    )
    st.stop()


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">✦ YOUR PERSONAL AI ASSISTANT</div>
        <h1>Conversations that <span>remember.</span></h1>
        <p>
            An intelligent chatbot powered by large language models.
            Ask questions, explore ideas, and continue your conversation
            without losing the context of what you said earlier.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


st.info(
    "✨ UI designed with AI assistance using Streamlit.",
    icon="🎨"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="status-card">
            <div class="status-label">Connection</div>
            <div class="status-value">
                <span class="status-dot"></span>Configured
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="status-card">
            <div class="status-label">Memory</div>
            <div class="status-value">🧠 Session Memory</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="status-card">
            <div class="status-label">Your Messages</div>
            <div class="status-value">
                {sum(
                    1 for message in st.session_state.messages
                    if message["role"] == "user"
                )}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )



if not st.session_state.messages:

    st.markdown(
        """
        <div class="welcome">
            <div class="welcome-icon">✧</div>
            <h2>What would you like to explore?</h2>
            <p>
                Start a conversation below. I'll use your previous
                messages as context for future replies in this session.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("##### ✨ Try asking")

    suggestion_cols = st.columns(3)

    suggestions = [
        "Explain machine learning simply",
        "Help me learn Python",
        "What is conversation memory?"
    ]

    for index, suggestion in enumerate(suggestions):
        with suggestion_cols[index]:
            if st.button(
                suggestion,
                key=f"suggestion_{index}",
                use_container_width=True
            ):
                st.session_state.pending_prompt = suggestion
                st.rerun()


# Display the existing conversation.
for index, message in enumerate(st.session_state.messages):

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if index < len(st.session_state.message_times):
            st.caption(st.session_state.message_times[index])


pending_prompt = st.session_state.pop("pending_prompt", None)

user_input = st.chat_input(
    "Message Memora AI...",
    key="chat_input"
)

if pending_prompt:
    user_input = pending_prompt


if user_input and user_input.strip():

    user_input = user_input.strip()

    with st.chat_message("user"):
        st.markdown(user_input)
        st.caption(datetime.now().strftime("%I:%M %p"))

    with st.spinner("us AI is thinking..."):

        try:
            reply = llm_client.get_llm_response(
                build_messages(
                    st.session_state.messages,
                    user_input
                )
            )

            if not isinstance(reply, str):
                reply = str(reply)

        except Exception as error:

            st.error(f"Unable to generate a response: {error}")

        else:

            current_time = datetime.now().strftime("%I:%M %p")

            st.session_state.messages.extend([
                {
                    "role": "user",
                    "content": user_input
                },
                {
                    "role": "assistant",
                    "content": reply
                }
            ])

            st.session_state.message_times.extend([
                current_time,
                current_time
            ])

            with st.chat_message("assistant"):
                st.markdown(reply)
                st.caption(current_time)



st.markdown(
    """
    <div class="footer">
        MEMORA AI · POWERED BY LANGCHAIN & STREAMLIT
        <br><br>
        Your conversation history stays in the current Streamlit session.
    </div>
    """,
    unsafe_allow_html=True
)