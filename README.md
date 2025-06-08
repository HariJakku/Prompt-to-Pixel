# 🖼️ GenAI Image Generator

A Streamlit app that generates images from text prompts using **Google Generative AI (Gemini 2.0)**.

---

## ✨ Features

- 🎨 Generate images based on user input text prompts  
- 💬 Displays AI-generated images and descriptive text  
- 🌗 Supports light and dark themes with a toggle  
- 📥 Allows downloading generated images in PNG format

---

## 🛠️ Tech Stack

- 🖥️ Streamlit  
- 🤖 Google GenAI API (Gemini 2.0 Flash Image Generation)  
- 🖼️ Pillow (PIL) for image processing

---
## 📂 Project Structure

```bash

├── img_gen.py               # Main Streamlit app
├── req.txt     # Python dependencies
├── image.png  # Output image (auto-generated)
└── README.md            # Project documentation
```
---

## ⚙️ Setup

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/genai-image-generator.git
    cd genai-image-generator
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r req.txt
    ```

4. Add your Google GenAI API key in `app.py`:
    ```python
    client = genai.Client(api_key="YOUR_API_KEY_HERE")
    ```

---

## ▶️ Running the App

```bash
streamlit run img_gen.py
