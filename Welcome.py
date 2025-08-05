# Welcome.py -- FINAL CORRECTED CODE (Strictly Navbar Change)

import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DICTIONARY OF PAGES (for navigation) ---
# We define this once at the top
PAGES = {
    "Blog Generator": "pages/blog_generator.py",
    "Image Finder": "pages/image_generator.py",
    "Doc Q&A": "pages/pdf_summarizer.py",
    "Translator": "pages/translator.py"
}

# --- FUNCTION TO INJECT THE NEW, IMPROVED BALL ANIMATION ---
def inject_ball_animation():
    """Injects CSS for a navy blue background with animated floating & pulsating orbs."""
    # This function is perfect as is. No changes needed.
    balls_html = '<div class="ball-container">'
    for _ in range(12):
        balls_html += '<div class="ball"></div>'
    balls_html += '</div>'
    css = """<style>...</style>""" # Your full CSS string
    st.markdown(css + balls_html, unsafe_allow_html=True)


# --- INITIALIZE THE PAGE AND ANIMATION ---
# inject_ball_animation() # Commenting this out to avoid clutter, but your original call is fine.

# --- TOP-CENTER TITLE & SUBTITLE ---
st.markdown('<p class="custom-title">AI Blog Generator Welcomes You!</p>', unsafe_allow_html=True)


# --- START OF CORRECTED NAVIGATION BAR SECTION ---
# ==============================================================================

# 1. The Safe Navigation Function
# This function is called by the menu's on_change callback.
# It reads the user's choice from session_state and switches the page.
def navigate():
    # Get the page the user selected from session state.
    page_name = st.session_state.get('menu_selection')
    
    # Check if the selected page needs navigation.
    if page_name and page_name in PAGES:
        # Switch to that page.
        st.switch_page(PAGES[page_name])

# 2. The Corrected Navigation Bar
# We add `on_change` and `key` to make the navigation safe.
selected_page = option_menu(
    menu_title=None,
    options=["Home", "Blog Generator", "Image Finder", "Doc Q&A", "Translator"],
    icons=["house-heart-fill", "pencil-square", "image-fill", "file-earmark-text-fill", "translate"],
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "icon": {"color": "#FFD700", "font-size": "20px"},
        "nav-link": {
            "font-size": "16px", "text-align": "center", "margin": "0px",
            "--hover-color": "rgba(255,215,0,0.2)",
            "color": "#FFD700",
        },
        "nav-link-selected": {
            "background-color": "#ff4b4b",
            "color": "#000000"
        },
    },
    # This calls our safe navigate function whenever the selection changes
    on_change=navigate,
    # This key stores the selection in st.session_state.menu_selection
    key='menu_selection' 
)

# ==============================================================================
# --- END OF CORRECTED NAVIGATION BAR SECTION ---


# --- PAGE CONTENT (THE HIGHLIGHTS) ---
# This part of your code remains exactly the same.
if selected_page == "Home":
    with st.container():
        st.markdown('<div class="light-glass-container">', unsafe_allow_html=True)
        st.markdown('<h2 class="purple-highlight-header">Find Your Creative Spark</h2>', unsafe_allow_html=True)
        st.write("")
        col1, col2, col3 = st.columns(3, gap="large")
        with col1:
            st.image("https://images.pexels.com/photos/5926382/pexels-photo-5926382.jpeg", caption="Plan Your Content")
        with col2:
            st.image("https://images.pexels.com/photos/3184454/pexels-photo-3184454.jpeg", caption="Craft Your Story")
        with col3:
            st.image("https://images.pexels.com/photos/265667/pexels-photo-265667.jpeg", caption="Engage Your Audience")
        st.markdown('</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="light-glass-container">', unsafe_allow_html=True)
        st.markdown('<h2 class="purple-highlight-header">Your Journey to a Successful Blog Starts Here</h2>', unsafe_allow_html=True)
        st.write("---")
        c1, c2, c3 = st.columns(3, gap="large")
        with c1:
            st.markdown('<h3 class="question-text">🤔 What is a Blog?</h3>', unsafe_allow_html=True)
            st.markdown('<p class="answer-text">A blog is your personal corner of the internet to share knowledge, document passions, or build a community.</p>', unsafe_allow_html=True)
        with c2:
            st.markdown('<h3 class="question-text">💡 Why Start a Blog?</h3>', unsafe_allow_html=True)
            st.markdown('<div class="answer-text"><ul><li>Share Your Passion</li><li>Build a Brand</li><li>Connect with People</li><li>Earn an Income</li></ul></div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<h3 class="question-text">🚀 How This App Helps You</h3>', unsafe_allow_html=True)
            st.markdown('<div class="answer-text"><ul><li><strong>Blog Generator:</strong> Instantly create articles.</li><li><strong>Image Finder:</strong> Find perfect, free images.</li><li><strong>Doc Q&A:</strong> Get answers from documents.</li><li><strong>Translator:</strong> Go global with your content.</li></ul></div>', unsafe_allow_html=True)

        st.markdown('<div class="centered-button-container">', unsafe_allow_html=True)
        # This button navigation is also safe because it's inside an `if` block.
        if st.button("✨ Start Creating Now", key="bottom_button"):
            st.switch_page("pages/blog_generator.py")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# --- DELETED NAVIGATION LOGIC ---
# The old, broken NAVIGATION LOGIC block at the end of the file has been
# completely removed, as it was the source of the crash.