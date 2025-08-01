# pages/2_🖼️_Image_Generator.py
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# --- Load the Pexels API Key ---
load_dotenv()
PEXELS_KEY = os.getenv("PEXELS_API_KEY")
API_URL = "https://api.pexels.com/v1/search" # The official Pexels API endpoint

# --- Helper Function for CSS ---
def load_css():
    """Injects custom CSS for an animated gradient background."""
    st.markdown("""
        <style>
            @keyframes gradient_animation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            .stApp {
                background: linear-gradient(-45deg, #a8c0ff, #3f2b96, #283c86, #45a247);
                background-size: 400% 400%;
                animation: gradient_animation 15s ease infinite;
            }
            .stButton>button {
                width: 100%;
            }
            .stDownloadButton>button {
                width: 100%;
                background-color: #4CAF50;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

# --- The function that uses the OFFICIAL Pexels API (Now with more options!) ---
def get_image_from_pexels_api(keywords, orientation="landscape", size="large"):
    """
    This function uses the stable, official Pexels API to get a relevant image.
    It now returns the full photo data dictionary or an error string.
    """
    if not PEXELS_KEY:
        return "ERROR: Pexels API Key not found. Please check your .env file."

    headers = {"Authorization": PEXELS_KEY}
    params = {
        "query": keywords,
        "per_page": 1,
        "orientation": orientation,
        "size": size,
    }
    
    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=15)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        
        data = response.json()
        if data["photos"]:
            # Return the entire first photo object
            return data["photos"][0]
        else:
            return "Error: No photos found for that query. Please try different keywords."
            
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Pexels API: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Image Finder", page_icon="🖼️", layout="wide")
load_css()

st.title("🖼️ Pexels Image Finder")

# Initialize session state to store the image data
if "pexels_data" not in st.session_state:
    st.session_state.pexels_data = None

# --- Main App Logic ---
if not PEXELS_KEY:
    st.error("CRITICAL ERROR: The Pexels API key is not configured. Please get a key from pexels.com/api and add it to your .env file.")
else:
    # Use columns for a cleaner layout
    col1, col2 = st.columns([1, 2]) # Control column is 1/3, Image column is 2/3

    with col1:
        st.subheader("🎨 Customize Your Image")
        image_keywords = st.text_input(
            "Enter keywords for the photo:", 
            placeholder="e.g., powerful lion standing brave"
        )
        
        orientation = st.selectbox(
            "Orientation:",
            ("landscape", "portrait", "square"),
            index=0
        )

        size = st.selectbox(
            "Size:",
            ("large", "medium", "small"),
            index=0,
            help="Note: 'large' is 24MP, 'medium' is 12MP, 'small' is 4MP. This does not refer to pixel dimensions."
        )

        generate_button = st.button("Find Photo", type="primary")

        if generate_button:
            if not image_keywords:
                st.warning("Please enter some keywords.")
                st.session_state.pexels_data = None # Clear previous image
            else:
                with st.spinner("Searching the Pexels library..."):
                    result = get_image_from_pexels_api(image_keywords, orientation, size)
                    if isinstance(result, dict):
                        st.session_state.pexels_data = result
                    else:
                        st.session_state.pexels_data = None # Clear previous on error
                        st.error(f"Could not retrieve an image. Details: {result}")

    with col2:
        if st.session_state.pexels_data:
            photo_data = st.session_state.pexels_data
            image_url = photo_data['src']['large2x'] # Use a high-res version for display
            photographer = photo_data['photographer']
            photographer_url = photo_data['photographer_url']
            pexels_url = photo_data['url']

            st.subheader("Your Image:")
            # --- THIS IS THE CORRECTED LINE ---
            st.image(image_url, use_container_width=True)
            
            # Attribution and Links
            st.markdown(f"**Photo by [{photographer}]({photographer_url}) on [Pexels]({pexels_url})**")
            
            # Download Button
            try:
                # Fetch the image content for the download button
                image_response = requests.get(image_url)
                image_bytes = image_response.content
                st.download_button(
                    label="📥 Download Photo",
                    data=image_bytes,
                    file_name=f"pexels_{photo_data['id']}.jpg",
                    mime="image/jpeg"
                )
            except Exception as e:
                st.error(f"Could not prepare image for download: {e}")

        else:
            st.info("Your generated image will appear here.")