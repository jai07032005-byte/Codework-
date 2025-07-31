# Gemini 1.5 Flash Powered Blog Generator

An AI-powered content creation suite built with Python and Streamlit. This app uses Google's Gemini 1.5 Flash to instantly generate blog posts, find images, analyze PDFs, and translate text.

![AI Blog Generator Screenshot](Blog.png)

---

### 🚀 Key Features
*   **AI Blog Generation:** Instantly create articles with Gemini 1.5 Flash.
*   **Image Finder:** Find images for your content via the Pexels API.
*   **Document Q&A:** Ask questions about your PDF documents.
*   **Text Translator:** Translate content to reach a wider audience.

---

### 🛠️ Technology Stack
*   **Python** & **Streamlit**
*   **APIs:** Google Gemini, OpenAI, Hugging Face, Pexels

---

### 🔧 How to Run This Project

#### 1. Clone the Repository
```bash
git clone https://github.com/jai07032005-byte/Codework-.git
cd Codework-

---

#### 3. Set Up API Keys
1.  Rename `env.template` to `.env`.
2.  Add your secret API keys to the `.env` file.
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    OPENAI_API_KEY="YOUR_API_KEY_HERE"
    HUGGINGFACE_API_KEY="YOUR_API_KEY_HERE"
    PEXELS_API_KEY="YOUR_API_KEY_HERE"
    ```
    *(**Important:** The `.gitignore` file ensures your `.env` file is never uploaded to GitHub.)*

#### 4. Run the Application
```bash
streamlit run Welcome.py