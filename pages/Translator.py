# pages/4_🌐_Translator.py
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- Load the Gemini API Key ---
try:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        GEMINI_CONFIGURED = False
    else:
        genai.configure(api_key=api_key)
        GEMINI_CONFIGURED = True
except Exception as e:
    GEMINI_CONFIGURED = False
    print(f"Error configuring Gemini: {e}")

# --- Helper Function for CSS ---
def load_css():
    """Injects custom CSS for an animated gradient background and other UI enhancements."""
    st.markdown("""
        <style>
            @keyframes gradient_animation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            .stApp {
                background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #373B44);
                background-size: 400% 400%;
                animation: gradient_animation 20s ease infinite;
                color: #E0E0E0;
            }
            .stTextArea textarea {
                background-color: rgba(255, 255, 255, 0.05);
                color: #FFFFFF;
                border-radius: 10px;
            }
            .stButton>button {
                width: 100%;
                border-radius: 20px;
                border: 1px solid #2c5364;
            }
        </style>
    """, unsafe_allow_html=True)

# --- The NEW Core Translation Function ---
def translate_text_with_gemini(source_text, source_lang, target_lang):
    """
    Uses the Gemini API to translate text between any two languages.
    """
    if not GEMINI_CONFIGURED:
        return "Error: Gemini API is not configured."

    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Create a dynamic, robust prompt
    if source_lang == "Auto-Detect":
        prompt = f"""
        You are a highly intelligent language identification and translation service.
        First, identify the language of the following text.
        Then, translate the identified text into {target_lang}.
        Provide ONLY the final translated text, without any explanation, headers, or the identified language name.
        If you cannot determine the language, respond with 'Error: Could not identify the source language.'

        Text to translate:
        ---
        {source_text}
        ---
        """
    else:
        prompt = f"""
        You are an expert translator. Your ONLY task is to translate the following text from {source_lang} into {target_lang}.
        Do not add any explanations, introductions, or any other text in your response.
        Provide ONLY the {target_lang} translation.

        {source_lang} Text:
        ---
        {source_text}
        ---
        """
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"An error occurred during translation: {e}"

# --- Language Options ---
LANGUAGES = {
    "Auto-Detect": "Auto-Detect",
    "English": "English",
    "Tamil": "Tamil",
    "Spanish": "Spanish",
    "French": "French",
    "German": "German",
    "Japanese": "Japanese",
    "Korean": "Korean",
    "Chinese (Simplified)": "Chinese (Simplified)",
    "Hindi": "Hindi",
    "Arabic": "Arabic"
}

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Universal Translator", page_icon="🌐", layout="wide")
load_css()

st.title("🌐 Universal Translator")
st.markdown("Translate text between multiple languages, powered by Google Gemini.")

# --- Initialize Session State ---
if 'source_text' not in st.session_state:
    st.session_state.source_text = ""
if 'translated_text' not in st.session_state:
    st.session_state.translated_text = ""
if 'source_lang' not in st.session_state:
    st.session_state.source_lang = "Auto-Detect"
if 'target_lang' not in st.session_state:
    st.session_state.target_lang = "Tamil"

# --- Main App Logic ---
if not GEMINI_CONFIGURED:
    st.error("CRITICAL ERROR: The Gemini API key is not configured. Please add it to your .env file and restart.")
else:
    # --- UI Layout: Language Selection and Swap Button ---
    col1, col2, col3 = st.columns([5, 1, 5])
    
    with col1:
        st.session_state.source_lang = st.selectbox(
            "From:", options=list(LANGUAGES.keys()), 
            key='select_source_lang', 
            index=list(LANGUAGES.keys()).index(st.session_state.source_lang)
        )
    
    with col2:
        st.write("") # for vertical alignment
        st.write("")
        if st.button("⇄", help="Swap languages"):
            # Swap languages
            source, target = st.session_state.source_lang, st.session_state.target_lang
            st.session_state.source_lang, st.session_state.target_lang = target, source
            # Swap text
            source_text, target_text = st.session_state.source_text, st.session_state.translated_text
            st.session_state.source_text, st.session_state.translated_text = target_text, source_text
            # Rerun to update UI
            st.rerun()

    with col3:
        # Filter out "Auto-Detect" from target languages
        target_lang_options = [lang for lang in LANGUAGES.keys() if lang != "Auto-Detect"]
        st.session_state.target_lang = st.selectbox(
            "To:", options=target_lang_options, 
            key='select_target_lang',
            index=target_lang_options.index(st.session_state.target_lang)
        )

    # --- UI Layout: Text Areas ---
    area1, area2 = st.columns(2)
    
    with area1:
        st.session_state.source_text = st.text_area(
            "Enter text to translate:", 
            value=st.session_state.source_text, 
            height=250, 
            key="source_text_area"
        )

    with area2:
        st.text_area(
            "Translated text:", 
            value=st.session_state.translated_text, 
            height=250, 
            key="translated_text_area",
            disabled=True
        )

    # --- Translate Button and Output Logic ---
    if st.button("Translate", type="primary"):
        if not st.session_state.source_text.strip():
            st.warning("Please enter some text to translate.")
        else:
            with st.spinner("Translating..."):
                translation_result = translate_text_with_gemini(
                    st.session_state.source_text,
                    st.session_state.source_lang,
                    st.session_state.target_lang
                )
                st.session_state.translated_text = translation_result
                st.rerun() # Rerun to update the disabled text area

    # --- Display with Copy Button if there is translated text ---
    if st.session_state.translated_text:
        if "Error:" in st.session_state.translated_text:
            st.error(st.session_state.translated_text)
        else:
            # Using st.code provides a built-in copy button!
            st.subheader("Result with Copy Option")
            st.code(st.session_state.translated_text, language=None)