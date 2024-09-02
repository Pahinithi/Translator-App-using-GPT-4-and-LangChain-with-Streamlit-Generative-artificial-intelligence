import streamlit as st
from translator_utils import translate

# Set the page configuration
st.set_page_config(
    page_title="Translator.AI",
    page_icon="🌐",
    layout="centered"
)

# Add custom CSS for styling
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #b869b6, #b86969, #69b86e);
            padding: 2rem;
            color: #333;
            font-family: 'Arial', sans-serif;
        }
        .stButton button {
            background-color: #69b86e;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-size: 1rem;
        }
        .stButton button:hover {
            background-color: #57a856;
        }
        .stTextInput textarea {
            border-radius: 8px;
            border: 1px solid #ccc;
            padding: 0.5rem;
            font-size: 1rem;
        }
        .stSelectbox, .stTextInput input {
            border-radius: 8px;
            border: 1px solid #ccc;
            padding: 0.5rem;
            font-size: 1rem;
        }
        .stTitle {
            color: #ffffff;
            margin-bottom: 2rem;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #ffffff;
            color: #333;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            box-shadow: 0px -2px 5px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

# Streamlit page title
st.title("🌐 Lanka Translator App - GPT-4")

col1, col2 = st.columns(2)

with col1:
    input_languages_list = ["English", "French", "German", "Latin", "Spanish", "Hindi", "Tamil", "Telugu", "Marathi"]
    input_language = st.selectbox(label="Input Language", options=input_languages_list)

with col2:
    output_languages_list = [x for x in input_languages_list if x != input_language]
    output_language = st.selectbox(label="Output Language", options=output_languages_list)

input_text = st.text_area("Type the text to be translated", height=150)

if st.button("Translate"):
    translated_text = translate(input_language, output_language, input_text)
    st.success(translated_text)

# Footer
st.markdown("""
    <div class="footer">
        Developed by Nithilan
    </div>
    """, unsafe_allow_html=True)
