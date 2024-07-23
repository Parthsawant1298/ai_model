import streamlit as st
import google.generativeai as genai
import PIL.Image
import os

# Configure API key from environment variable

genai.configure(api_key="AIzaSyDoR10wPWSnCCLXHZWWrlrAg7XCXFzzpx8")

# Function to generate content using Google Generative AI
def generate_content_from_image(image):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(["What is in this photo?", image])
    return response.text

# Streamlit App
st.title("Image Content Generator")

# Upload image file
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open and display the uploaded image
    img = PIL.Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    if st.button("Generate Content"):
        try:
            # Generate content based on the uploaded image
            content = generate_content_from_image(img)
            st.text_area("Generated Content:", value=content, height=200)
        except Exception as e:
            st.error(f"Error generating content: {e}")
else:
    st.info("Please upload an image to get started.")
