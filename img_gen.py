import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="🖼️ Image Gen with GenAI", page_icon="🤖")
# Theme toggle
theme = st.radio("🌗 Choose Theme:", ["🌞 Light", "🌚 Dark"], horizontal=True)

# Theme-based colors and emojis
title_emoji = "🖼️" if theme == "🌞 Light" else "🖼️"
prompt_emoji = "📝"
generate_emoji = "✨"
success_emoji = "✅"
warning_emoji = "⚠️"
error_emoji = "❌"
spinner_emoji = "⏳"
download_emoji = "⬇️"
info_emoji = "ℹ️"

# Optional background color for dark mode
if theme == "🌚 Dark":
    st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

st.title("🖼️ AI-Driven Visual Generation")
st.markdown("🎯 Experience the power of Generative AI—Create stunning visuals from your imagination using Google's cutting-edge technology.")

contents = st.text_area("📝 Enter your prompt here:", height=100, placeholder="Type something creative...")

if st.button("✨ Generate Image"):
    if not contents:
        st.error("⚠️ Please enter a text prompt.")
    else:
        with st.spinner("⏳ Generating Image... Please wait"):
            try:
                client = genai.Client(api_key="Your-api-key")  
                response = client.models.generate_content(
                    model="gemini-2.0-flash-preview-image-generation",
                    contents=contents,
                    config=types.GenerateContentConfig(
                        response_modalities=['TEXT', 'IMAGE']
                    )
                )
                if response.candidates and len(response.candidates) > 0:
                    text_found = False
                    image_found = False
                    for part in response.candidates[0].content.parts:
                        if hasattr(part, "text") and part.text is not None:
                            st.markdown("### 💬 Model Response")
                            st.write(part.text)
                            text_found = True
                        elif hasattr(part, "inline_data") and part.inline_data is not None:
                            try:
                                image = Image.open(BytesIO(part.inline_data.data))
                                st.markdown("### 🖼️ Generated Image")
                                st.image(image, caption="🖌️ AI-Generated Art", use_container_width=True)

                                image.save("gemini-native-image.png")
                                img_buffer = BytesIO()
                                image.save(img_buffer, format="PNG")
                                img_buffer.seek(0)

                                st.download_button(
                                    label="⬇️ Download Image",
                                    data=img_buffer.getvalue(),
                                    file_name="gemini-native-image.png",
                                    mime="image/png"
                                )
                                image_found = True
                                st.success("✅ Image generated successfully!")
                            except Exception as e:
                                st.error(f"❌ Error processing image: {e}")
                    if not text_found and not image_found:
                        st.warning("⚠️ No text or image found in the response.")
                else:
                    st.error("🚫 No response from the model.")
            except Exception as e:
                st.error(f"❗An error occurred while generating content: {e}")

with st.expander("ℹ️ About"):
    st.markdown("""
    📌 This application uses **Google GenAI** to generate images based on user-provided text prompts.  
    ✏️ Enter a creative prompt, and the AI will generate a related image just for you!

    🔐 **Note:** Ensure you have a valid API key and the required permissions to use Google GenAI services.
    """)
