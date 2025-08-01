# pages/1_✍️_Blog_Generator.py
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- Core Functionality ---
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

try:
    genai.configure(api_key=GEMINI_API_KEY)
    GEMINI_CONFIGURED = True
except Exception as e:
    GEMINI_CONFIGURED = False
    print(f"Error configuring Gemini: {e}")

# --- AI Generation Functions ---

def generate_blog_content(topic, keywords, length, tone, audience, cta):
    """Generates the main blog post content."""
    prompt = f"""
        You are a world-class blog writer, content strategist, and SEO expert. Your task is to write a comprehensive, engaging, and well-structured blog post.

        **Primary Topic:** "{topic}"
        **Keywords to strategically integrate:** "{keywords}"
        **Target Audience:** "{audience}"
        **Tone of Voice:** "{tone}"
        **Target Length:** Approximately {length} words.
        **Call to Action:** Conclude the blog post by naturally incorporating this call to action: "{cta}"

        **Strict Structure Requirements:**
        - **Main Title (H1):** Start with one, and only one, H1 title (using a single # in markdown). The title must be catchy, SEO-friendly, and directly related to the topic.
        - **Introduction:** A short, compelling introduction that hooks the reader and states the blog's purpose.
        - **Body Content:** Use multiple H2 headings (##) to divide the main sections. Use H3 subheadings (###) where necessary for more detailed points. Use lists, bold text, and italics to improve readability.
        - **Conclusion:** Provide a concise summary of the key points and seamlessly integrate the call to action.

        **Output Format:** Return ONLY the raw markdown text for the blog post. Do not include any of your own commentary before or after the markdown content.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error from Gemini API: {str(e)}"

def generate_accompanying_content(blog_post_content, topic, keywords):
    """Generates SEO analysis, social posts, and an image prompt based on the blog."""
    prompt = f"""
        You are a multi-disciplinary AI assistant specializing in content marketing. Based on the following blog post, generate the requested accompanying assets.

        **Blog Post Content:**
        ---
        {blog_post_content}
        ---

        **Main Topic:** "{topic}"
        **Keywords:** "{keywords}"

        **Tasks to Perform:**

        1.  **SEO Analysis:**
            -   **Meta Description:** Write a compelling, SEO-optimized meta description (155-160 characters).
            -   **Keyword Analysis:** Briefly analyze how well the main keywords were integrated.
            -   **Title Suggestion:** Offer one alternative, catchy title for A/B testing.

        2.  **Social Media Posts:**
            -   **Twitter/X Post:** A short, punchy tweet with relevant hashtags.
            -   **LinkedIn Post:** A more professional post, suitable for a business audience, encouraging discussion.
            -   **Facebook Post:** An engaging post that asks a question to drive comments.

        3.  **Image Prompt:**
            -   **Featured Image Idea:** Write a descriptive prompt for an AI image generator (like Midjourney or DALL-E) to create a high-quality featured image for this blog. Be specific about style, composition, colors, and mood.

        **Output Format:** Return the response as a single block of markdown, using H2 (##) for each main section (SEO Analysis, Social Media Posts, Image Prompt) and H3 (###) for sub-sections.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error from Gemini API: {str(e)}"

# --- Custom UI Styling (CSS) ---
st.set_page_config(page_title="Blog Generator Pro", page_icon="✍️", layout="wide")
st.markdown("""<style>... </style>""", unsafe_allow_html=True) # Your full CSS block goes here

# --- Streamlit Page Layout ---
with st.sidebar:
    # Your sidebar code is perfect and remains unchanged
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.header("✨ Blog Configuration")
    blog_topic = st.text_input("Blog Topic", placeholder="e.g., The Future of AI", key="topic")
    # ... rest of your sidebar code ...
    blog_keywords = st.text_area("Keywords (comma separated)", placeholder="e.g., machine learning, innovation", key="keywords")
    blog_length = st.slider("Approximate word count", 250, 2000, 750, 250, key="length")
    with st.expander("Advanced Options"):
        tone_of_voice = st.selectbox("Tone of Voice",("Professional", "Casual", "Humorous", "Authoritative", "Inspirational"),key="tone")
        target_audience = st.text_input("Target Audience", placeholder="e.g., Tech Entrepreneurs", key="audience")
        call_to_action = st.text_input("Call to Action", placeholder="e.g., Subscribe to our newsletter!", key="cta")
    st.write("---")
    generate_button = st.button("Generate Content Suite", use_container_width=True)

# Main content area
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Session state initialization
if 'blog_post' not in st.session_state:
    st.session_state.blog_post = ""
if 'accompanying_content' not in st.session_state:
    st.session_state.accompanying_content = ""

if generate_button:
    if not GEMINI_CONFIGURED:
        st.error("Gemini API is not configured. Please check your API key.")
    elif not blog_topic or not blog_keywords:
        st.warning("Please provide a topic and keywords in the sidebar.")
    else:
        with st.spinner("Your AI is crafting the content suite... This may take a moment."):
            st.session_state.blog_post = generate_blog_content(blog_topic, blog_keywords, blog_length, tone_of_voice, target_audience, call_to_action)
            # We will only generate accompanying content if the blog post was successful
            if "Error" not in st.session_state.blog_post and st.session_state.blog_post:
                st.session_state.accompanying_content = generate_accompanying_content(st.session_state.blog_post, blog_topic, blog_keywords)
            else:
                st.session_state.accompanying_content = "" # Clear old content on failure

# Display the generated content or a placeholder
if st.session_state.blog_post and "Error" not in st.session_state.blog_post:
    st.success("Your content suite has been generated successfully!")
    
    tab1, tab2, tab3 = st.tabs(["✍️ Blog Post", "📊 SEO & Social", "🖼️ Image Idea"])

    with tab1:
        st.subheader("Generated Blog Post")
        st.markdown(f'<div class="generated-content-area">{st.session_state.blog_post}</div>', unsafe_allow_html=True)
        st.download_button(
            label="📥 Download Blog as Markdown",
            data=st.session_state.blog_post,
            file_name=f"{blog_topic.replace(' ', '_').lower()}_blog.md",
            mime="text/markdown",
        )

    with tab2:
        st.subheader("SEO Analysis & Social Media Posts")
        # ULTIMATE SAFETY CHECK: Only proceed if accompanying content exists and is not an error
        if st.session_state.accompanying_content and "Error" not in st.session_state.accompanying_content:
            if "## Image Prompt" in st.session_state.accompanying_content:
                seo_content = st.session_state.accompanying_content.split("## Image Prompt")[0]
                st.markdown(seo_content)
            else:
                st.markdown(st.session_state.accompanying_content) # Display all of it if separator isn't found
        elif "Error" in st.session_state.accompanying_content:
            st.error(f"Could not generate SEO/Social content: {st.session_state.accompanying_content}")
        else:
            st.info("SEO & Social content will appear here.")
            
    with tab3:
        st.subheader("AI Featured Image Prompt")
        # ULTIMATE SAFETY CHECK for this tab
        if st.session_state.accompanying_content and "Error" not in st.session_state.accompanying_content:
            if "## Image Prompt" in st.session_state.accompanying_content:
                image_prompt_full_section = st.session_state.accompanying_content.split("## Image Prompt", 1)[1]
                st.markdown("## Image Prompt" + image_prompt_full_section)
                prompt_text_only = image_prompt_full_section.replace("Featured Image Idea", "").strip()
                parts = prompt_text_only.split(":", 1)
                
                if len(parts) > 1 and parts[1].strip():
                    actual_prompt = parts[1].strip()
                    st.code(actual_prompt, language=None)
                else:
                    st.warning("Could not automatically extract a clean prompt. The full AI-generated text is shown above.")
            else:
                st.error("The AI did not generate an 'Image Prompt' section this time.")
        elif "Error" in st.session_state.accompanying_content:
            st.error(f"Could not generate an image prompt: {st.session_state.accompanying_content}")
        else:
            st.info("The image prompt idea will appear here.")
            
elif "Error" in st.session_state.blog_post:
    st.error(st.session_state.blog_post)

else:
    placeholder_html = """
    <div class="generated-content-area" style="text-align: center; padding: 4rem 2rem;">
        <h1>Welcome to the Blog Generator Pro</h1>
        <h2>Your complete content creation suite awaits.</h2>
        <p style="color: #E0E0E0;">Fill in the details on the left sidebar and click 'Generate Content Suite' to see the magic happen!</p>
    </div>
    """
    st.markdown(placeholder_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)