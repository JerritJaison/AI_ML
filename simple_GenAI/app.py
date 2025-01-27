#putting app py
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
import base64
my_api_key = "AIzaSyBI0We1YJCfqYOXV_jukqu2CEVG98m2f2I"  
genai.configure(api_key=my_api_key)
#genai.configure(api_key=os.getenv('AIzaSyBI0We1YJCfqYOXV_jukqu2CEVG98m2f2I'))

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response= model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A Demo")

st.header("Hi i am Nihal, girl's personal companion ")

first = st.text_input("Are you a girl ",key="first")
enter =st.button("Enter")
if enter:
    if(first == 'yes'):
        st.balloons()
     
        input = st.text_input("Input: ",key="input")
        name = st.text_input("Enter Your name ",key="name")
        submit = st.button("Ask the question")

        if submit:
            st.write(f'Hello {name}\n This is your output')
            # st.write(f'Since it is for {reason} purpose we are allowing your request')
            response=get_gemini_response(input)
            st.subheader("The response is")
            st.write(response)
    else:
        st.write("Sorry only girls are allowed")

# to run -> streamlit run c:/Users/jerri/OneDrive/Documents/AI_ML/simple_GenAI/app.py
# to create environment -> conda create -n {name}

#background change to image
def set_bg_hack(main_bg):
    """
    A function to set a background image for the main panel in Streamlit.

    Args:
        main_bg: The path to the background image file.
    """
    main_bg_ext = "jpeg"  # Replace with the actual extension of your image file

    # Encode the image as a base64 string
    with open(main_bg, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    # Set the background image using CSS
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{main_bg_ext};base64,{encoded_string});
            background-size: cover; 
            
        }}
        </style>
        
        """,
        unsafe_allow_html=True,
    )


# Path to your background image
background_img = r"C:\Users\jerri\Downloads\jaggu.jpeg" 

# Set the background image
set_bg_hack(background_img)
#--------------------------------------------------------------------

# input = st.text_input("Input Prompt: ",key="input")

# uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

# image = ""

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image.",use_column_width=True)

# submit=st.button("Tell me about the image")

# #if button clicked...

# response = get_gemini_response(input,image)
# st.subheader("The Response is")
# st.write(response)