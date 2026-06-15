import sys
import os
import tempfile

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st
from streamlit_mic_recorder import mic_recorder

from assistant.predict import predict_intent
from assistant.actions import perform_action
from assistant.transcribe import transcribe_audio

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="AI Voice Assistant",
    page_icon="🎙️",
    layout="wide"
)

# ====================================
# CUSTOM CSS
# ====================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 50%,
        #334155 100%
    );
}

.main-title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:white;
    margin-bottom:10px;
}

.sub-title{
    text-align:center;
    color:#cbd5e1;
    font-size:20px;
    margin-bottom:30px;
}

.glass-card{
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(15px);
    border-radius:20px;
    padding:20px;
    margin-bottom:20px;
    border:1px solid rgba(255,255,255,0.15);
}

.history-box{
    background:rgba(255,255,255,0.08);
    border-radius:15px;
    padding:15px;
    margin-bottom:10px;
    border-left:5px solid #3b82f6;
}

.stButton > button{
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    color:white;
    background:linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
}

.stTextInput input{
    border-radius:12px;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ====================================
# HEADER
# ====================================

st.markdown(
    '<div class="main-title">🎙️ AI Voice Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Machine Learning Powered Smart Voice Assistant</div>',
    unsafe_allow_html=True
)

# ====================================
# BANNER IMAGE
# ====================================

banner_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "assets",
    "banner.jpg"
)

if os.path.exists(banner_path):
    st.image(
        banner_path,
        use_container_width=True
    )

# ====================================
# SESSION STATE
# ====================================

if "history" not in st.session_state:
    st.session_state.history = []

# ====================================
# STATUS CARDS
# ====================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Assistant",
        "Online ✅"
    )

with col2:
    st.metric(
        "ML Model",
        "Loaded ✅"
    )

with col3:
    st.metric(
        "Voice Engine",
        "Ready ✅"
    )

# ====================================
# TEXT COMMAND
# ====================================

st.markdown("""
<div class="glass-card">
<h3>⌨️ Text Command</h3>
</div>
""", unsafe_allow_html=True)

command = st.text_input(
    "Enter Command",
    placeholder="Example: open calculator"
)

if st.button("🚀 Execute Text Command"):

    if command.strip():

        intent = predict_intent(
            command.lower()
        )

        response = perform_action(
            intent,
            command.lower()
        )

        st.success(
            f"Intent Detected: {intent}"
        )

        st.info(
            response
        )

        st.session_state.history.append(
            (command, response)
        )

# ====================================
# VOICE COMMAND
# ====================================

st.markdown("""
<div class="glass-card">
<h3>🎤 Voice Command</h3>
<p>Click Start Recording and speak your command.</p>
</div>
""", unsafe_allow_html=True)

audio = mic_recorder(
    start_prompt="🎙️ Start Recording",
    stop_prompt="⏹️ Stop Recording",
    key="voice_recorder"
)

if audio and "bytes" in audio:

    try:

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp_audio:

            temp_audio.write(
                audio["bytes"]
            )

            audio_path = temp_audio.name

        with st.spinner(
            "Transcribing speech..."
        ):

            text = transcribe_audio(
                audio_path
            )

        st.write("### 🗣 You Said")

        st.success(
            text
        )

        intent = predict_intent(
            text
        )

        response = perform_action(
            intent,
            text
        )

        st.write(
            "### 🤖 Assistant Response"
        )

        st.info(
            response
        )

        st.session_state.history.append(
            (text, response)
        )

        if os.path.exists(audio_path):
            os.remove(audio_path)

    except Exception as e:

        st.error(
            f"Voice Processing Error: {e}"
        )

# ====================================
# COMMAND HISTORY
# ====================================

st.markdown("""
<div class="glass-card">
<h3>📜 Command History</h3>
</div>
""", unsafe_allow_html=True)

if len(st.session_state.history) == 0:

    st.info(
        "No commands executed yet."
    )

for command, response in reversed(
        st.session_state.history):

    st.markdown(
        f"""
        <div class="history-box">
            <b>🗣 User Command</b><br>
            {command}
            <br><br>
            <b>🤖 Assistant Response</b><br>
            {response}
        </div>
        """,
        unsafe_allow_html=True
    )

# ====================================
# FOOTER
# ====================================

st.markdown("---")

st.markdown(
    """
    <center>
        <h4>AI Voice Assistant using Machine Learning</h4>
        <p>
            Built with Python, Streamlit, Whisper,
            Scikit-Learn and Natural Language Processing
        </p>
    </center>
    """,
    unsafe_allow_html=True
)