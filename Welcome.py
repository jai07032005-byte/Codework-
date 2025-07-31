import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- FUNCTION TO INJECT THE NEW, IMPROVED BALL ANIMATION ---
def inject_ball_animation():
    """Injects CSS for a navy blue background with animated floating & pulsating orbs."""

    balls_html = '<div class="ball-container">'
    for _ in range(12):
        balls_html += '<div class="ball"></div>'
    balls_html += '</div>'

    # The CSS has been updated with a new animation and ball style.
    css = """
    <style>
        /* --- 1. NAVY BLUE BACKGROUND (Unchanged) --- */
        .stApp {
            background: #0f172a;
            color: #FFFFFF;
        }

        /* --- 2. ORB/BALL CONTAINER (Unchanged) --- */
        .ball-container {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none; overflow: hidden; z-index: -1;
        }

        /* --- 3. [NEW] KEYFRAME ANIMATION FOR FLOATING, DRIFTING & PULSATING --- */
        @keyframes animate-orb {
            0% {
                transform: translateY(0) translateX(0) scale(1);
                opacity: 0.8;
            }
            25% {
                transform: translateY(-25vh) translateX(30px) scale(1.05);
            }
            50% {
                transform: translateY(-50vh) translateX(-25px) scale(1);
                opacity: 0.5;
            }
            75% {
                 transform: translateY(-75vh) translateX(20px) scale(1.05);
            }
            100% {
                transform: translateY(-120vh) translateX(0) scale(1.1);
                opacity: 0;
            }
        }

        /* --- 4. [NEW] INDIVIDUAL ORB STYLING (IMPROVED LOOK) --- */
        .ball {
            position: absolute;
            display: block;
            list-style: none;
            width: 20px;
            height: 20px;
            /* New 3D look with a radial gradient */
            background: radial-gradient(circle at 30% 30%, rgba(173, 216, 230, 0.9), rgba(109, 213, 237, 0.5) 90%);
            border-radius: 50%;
            /* New softer glow effect */
            box-shadow: 0 0 15px rgba(109, 213, 237, 0.7),
                        0 0 25px rgba(109, 213, 237, 0.5),
                        inset 0 0 4px rgba(255, 255, 255, 0.6);
            /* Applying the new, more dynamic animation */
            animation: animate-orb 25s infinite linear;
            bottom: -150px; /* Start below the screen */
        }

        /* --- 5. GIVING EACH ORB A UNIQUE ANIMATION (Unchanged Logic, New Effect) --- */
        .ball:nth-child(1) { left: 25%; width: 80px; height: 80px; animation-delay: 0s; }
        .ball:nth-child(2) { left: 10%; width: 20px; height: 20px; animation-delay: 2s; animation-duration: 12s; }
        .ball:nth-child(3) { left: 70%; width: 20px; height: 20px; animation-delay: 4s; }
        .ball:nth-child(4) { left: 40%; width: 60px; height: 60px; animation-delay: 0s; animation-duration: 18s; }
        .ball:nth-child(5) { left: 65%; width: 20px; height: 20px; animation-delay: 0s; }
        .ball:nth-child(6) { left: 75%; width: 110px; height: 110px; animation-delay: 3s; }
        .ball:nth-child(7) { left: 35%; width: 150px; height: 150px; animation-delay: 7s; }
        .ball:nth-child(8) { left: 50%; width: 25px; height: 25px; animation-delay: 15s; animation-duration: 45s; }
        .ball:nth-child(9) { left: 20%; width: 15px; height: 15px; animation-delay: 2s; animation-duration: 35s; }
        .ball:nth-child(10) { left: 85%; width: 150px; height: 150px; animation-delay: 0s; animation-duration: 11s; }

        /* --- ALL YOUR OTHER STYLES ARE PRESERVED EXACTLY AS THEY WERE --- */
        header, footer { visibility: hidden !important; }
        .custom-title { font-family: 'Times New Roman', Times, serif; font-size: 90px !important; font-weight: 900 !important; color: #FFFFFF; text-align: center; padding-top: 2rem; padding-bottom: 1rem; line-height: 1.1; text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5); }
        div[data-testid="stOptionMenu"] > div { background-color: rgba(0, 0, 0, 0.4) !important; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.1); }
        .light-glass-container { padding: 2.5rem; background-color: rgba(255, 255, 255, 0.1); border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2); margin: 2rem 0; }
        .purple-highlight-header { color:#6dd5ed; font-weight: 700; text-align: left; }
        .question-text { color: #FFFFFF !important; font-size: 1.75rem; font-weight: 600; }
        .answer-text, .answer-text li, .answer-text strong { color: #E0E0E0 !important; font-size: 1rem; }
        [data-testid="stImageCaption"] { color: #A0BBD0 !important; }
        .stImage > img { border-radius: 15px; }
        .centered-button-container { text-align: center; margin-top: 2.5rem; }
        .stButton > button { border: none; border-radius: 25px; padding: 0.8rem 1.8rem; color: #000000; background-color: #ff4b4b; font-weight: bold; font-size: 1.1rem; transition: all 0.3s ease-in-out; }
        .stButton > button:hover { transform: scale(1.05); }
    </style>
    """
    st.markdown(css + balls_html, unsafe_allow_html=True)


# --- INITIALIZE THE PAGE AND ANIMATION ---
inject_ball_animation()

# --- TOP-CENTER TITLE & SUBTITLE ---
st.markdown('<p class="custom-title">AI Blog Generator Welcomes You!</p>', unsafe_allow_html=True)


# --- NAVIGATION BAR ---
selected_page = option_menu(
    menu_title=None,
    options=["Home", "Blog Generator", "Image Finder", "Doc Q&A", "Translator"],
    icons=["house-heart-fill", "pencil-square", "image-fill", "file-earmark-text-fill", "translate"],
    menu_icon="cast", default_index=0, orientation="horizontal",
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
    }
)


# --- PAGE CONTENT (THE HIGHLIGHTS) ---
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
        if st.button("✨ Start Creating Now", key="bottom_button"):
            st.switch_page("pages/blog_generator.py")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
PAGES = {
    "Blog Generator": "pages/blog_generator.py",
    "Image Finder": "pages/image_generator.py",
    "Doc Q&A": "pages/pdf_summarizer.py",
    "Translator": "pages/translator.py"
}

if selected_page in PAGES:
    st.switch_page(PAGES[selected_page])