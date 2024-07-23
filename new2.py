import streamlit as st
import google.generativeai as genai
import pandas as pd
import io
import os

# Configure API key directly (for demonstration purposes)
genai.configure(api_key="AIzaSyDoR10wPWSnCCLXHZWWrlrAg7XCXFzzpx8")

# Function to generate dataset based on a text prompt using Google Generative AI
def generate_dataset_from_text(text):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(["Generate a dataset in CSV format based on the following text with out explaination just data:", text])
    return response.text

# Function to clean CSV data for parsing
def clean_csv_data(csv_data):
    # Simple cleaning to handle common issues
    lines = csv_data.splitlines()
    cleaned_lines = []
    
    for line in lines:
        # Remove any leading or trailing whitespace and ensure consistent delimiters
        cleaned_line = line.strip()
        cleaned_lines.append(cleaned_line)
    
    return "\n".join(cleaned_lines)

# Streamlit App
st.title("Dataset Generator from Text")

# Input field for text prompt
text_prompt = st.text_area("Enter a prompt to generate dataset:", height=150)

if st.button("Generate Dataset"):
    if text_prompt:
        try:
            # Generate dataset from the text prompt
            csv_data = generate_dataset_from_text(text_prompt)
            
            # Clean the CSV data
            cleaned_csv_data = clean_csv_data(csv_data)
            
            # Print CSV data for debugging
            st.text_area("Generated CSV Data:", value=cleaned_csv_data, height=200)
            
            # Try to convert CSV data into a DataFrame
            try:
                df = pd.read_csv(io.StringIO(cleaned_csv_data))
                st.dataframe(df)
                
                # Provide download options for the generated CSV
                st.download_button("Download CSV", cleaned_csv_data, file_name='generated_dataset.csv', mime='text/csv')
            except pd.errors.ParserError:
                st.error("Error parsing CSV data. The cleaned CSV might still be incorrectly formatted.")
            
        except Exception as e:
            st.error(f"Error generating dataset: {e}")
    else:
        st.warning("Please provide a text prompt.")
