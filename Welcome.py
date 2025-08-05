import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
# Using "auto" for the sidebar makes it expanded on desktop and collapsed on mobile.
st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="auto"  # This is key for responsiveness
)

# --- FUNCTION TO INJECT CSS AND BACKGROUND ---
# We no longer need responsive navbar CSS, just styles for the page and background.
def inject_css_and_background():
    """
    Injects CSS for page styling and the animated orb background.
    """
    # HTML for the animated background orbs
    balls_html = '<div class="ball-container">' + ''.join(['<div class="ball"></div>' for _ in range(12)]) + '</div>'

    # The simplified CSS for the page
    css = """
    <style>
        /* --- Hide Streamlit's default header, footer, and hamburger menu --- */
        /* The sidebar will have its own menu functionality */
        header, footer { visibility: hidden !important; }
        .st-emotion-cache-18ni7ap { display: none; } /* Hides default hamburger */

        /* --- General and Background Styles --- */
        .stApp { background: #0f172a; color: #FFFFFF; }
        .ball-container { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; overflow: hidden; z-index: -1; }
        @keyframes animate-orb {
            0% { transform: translateY(0) translateX(0) scale(1); opacity: 0.8; }
            50% { transform: translateY(-50vh) translateX(-25px) scale(1); opacity: 0.5; }
            100% { transform: translateY(-120vh) translateX(0) scale(1.1); opacity: 0; }
        }
        .ball { /* Orb styles remain the same */
            position: absolute; display: block; list-style: none; width: 20px; height: 20px;
            background: radial-gradient(circle at 30% 30%, rgba(173, 216, 230, 0.9), rgba(109, 213, 237, 0.5) 90%);
            border-radius: 50%;
            box-shadow: 0 0 15px rgba(109, 213, 237, 0.7), 0 0 25px rgba(109, 213, 237, 0.5), inset 0 0 4px rgba(255, 255, 255, 0.6);
            animation: animate-orb 25s infinite linear;
            bottom: -150px;
        }
        /* Add other ball styles as needed */
        .ball:nth-child(1) { left: 25%; width: 80px; height: 80px; animation-delay: 0s; }
        .ball:nth-child(2) { left: 10%; width: 20px; height: 20px; animation-delay: 2s; animation-duration: 12s; }
        /* ... etc. for all 10 balls ... */

        /* --- Main Content Styling --- */
        .custom-title {
            font-family: 'Times New Roman', Times, serif; font-size: 80px !important; font-weight: 900 !important;
            color: #FFFFFF; text-align: center; padding-top: 1rem; padding-bottom: 2rem;
            line-height: 1.1; text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
        }
        .light-glass-container {
            padding: 2.5rem; background-color: rgba(255, 255, 255, 0.05);
            border-radius: 15px; backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1); margin: 1rem 0;
        }
        .purple-highlight-header { text-align: center; color: #E0B0FF; }
        .question-text { color: #FFD700; }
        .answer-text, .answer-text ul li { color: #FFFFFF; }
        .centered-button-container { text-align: center; margin-top: 2rem; }

        /* --- Sidebar Styling --- */
        [data-testid="stSidebar"] {
            background-color: #0f172a; /* Match the main background */
            border: none;
        }
    </style>
    """
    st.markdown(css + balls_html, unsafe_allow_html=True)

# --- START OF APP ---
inject_css_and_background()

# --- NAVIGATION MENU (IN THE SIDEBAR) ---
# By placing the menu in st.sidebar, Streamlit handles the responsiveness automatically.
with st.sidebar:
    selected_page = option_menu(
        menu_title="Navigation",  # Title for the sidebar menu
        options=["Home", "Blog Generator", "Image Finder", "Doc Q&A", "Translator"],
        icons=["house-heart-fill", "pencil-square", "image-fill", "file-earmark-text-fill", "translate"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0f172a"},
            "icon": {"color": "#FFD700", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px", "text-align": "left", "margin": "5px",
                "--hover-color": "rgba(255,215,0,0.2)",
                "color": "#FFD700",
            },
            "nav-link-selected": {"background-color": "#ff4b4b", "color": "#FFFFFF"},
        }
    )

# --- PAGE CONTENT (Displayed based on selection) ---
if selected_page == "Home":
    st.markdown('<p class="custom-title">AI Blog Generator Welcomes You!</p>', unsafe_allow_html=True)

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
        if st.button("✨ Start Creating Now", key="bottom_button"):
            # To navigate, we simply call st.switch_page
            st.switch_page("pages/Blog_generator.py")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
# Define the mapping from page names to file paths
PAGES = {
    "Blog Generator": "pages/Blog_generator.py",
    "Image Finder": "pages/Image_generator.py",
    "Doc Q&A": "pages/pdf_summarizer.py",
    "Translator": "pages/Translator.py"
}

# If the selected page is one of the other pages (not "Home"), switch to it.
if selected_page in PAGES:
    st.switch_page(PAGES[selected_page])