import streamlit as st
import google.generativeai as genai

# Configure Gemini with API key
genai.configure(api_key="AIzaSyBy0nEMHwDwImc0ySdDRIZfVVGkuzzgX9E")

def generate_business_names(input_text):
    # Prompt for Gemini model
    prompt = f"""
        You are a creative consultant specializing in e-commerce branding and marketing. 
        Your task is to generate unique and catchy e-commerce business names based on the provided details: "{input_text}".
        Aim to capture the essence and appeal of the business in the generated names. 
        Please ensure that the names are suitable for branding and easily memorable by potential customers.
        """
    # Use Gemini to generate product names and descriptions
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit App
st.set_page_config(page_title="E-commerce Business Name Generator")

# Center the main content
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main title and description
st.title("E-commerce Business Name Generator")
st.write("Enter details about your e-commerce business and generate creative business names!")

# Center the text area
st.markdown(
    """
    <style>
    .text-area-container {
        width: 50%;
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 10px;
        margin: auto;
        resize: vertical;
        min-height: 150px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# User input for business details
business_details = st.text_area("Enter details about your e-commerce business:", height=150, max_chars=500, key="text_area")

generate_names = st.button("Generate Business Names")

if generate_names:
    if business_details:
        try:
            with st.spinner("Generating business names..."):
                business_names = generate_business_names(business_details)
            st.subheader("Creative Business Names:")
            st.write(business_names)
        except Exception as e:
            st.error("An error occurred while generating business names. Please try again later.")
    else:
        st.warning("Please enter details about your e-commerce business.")
