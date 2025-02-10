#putting app py
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
import base64
import speech_recognition as sr
import wikipedia
import pyjokes
import voice as v


my_api_key = "your key"  
genai.configure(api_key=my_api_key)
#genai.configure(api_key=os.getenv('AIzaSyBI0We1YJCfqYOXV_jukqu2CEVG98m2f2I'))

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    try:

        response= model.generate_content(f"{question}Answer exactly in 3 sentence")
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

st.set_page_config(page_title="Q&A Demo")

st.header("Hi i am Nihal, Your Personal Assistant")

     
# input = st.text_input("Input: ",key="input")
# name = st.text_input("Enter Your name ",key="name")
# submit = st.button("Ask the question")
v.username()

#st.write(f'Hello {name}\n This is your output')
# st.write(f'Since it is for {reason} purpose we are allowing your request')
while True:

    query = v.getcommand().lower()

    if "who made you" in query or "who created you" in query: 
        v.speak("Great question.")
        v.speak("I have been created by Jerrit Jaison. for your assistance.")
             
    elif 'joke' in query:
        v.speak(pyjokes.get_joke())
    elif 'play music' in query or "play song" in query:
        v.speak("Here you go with music")
        # music_dir = "G:\\Song"
        music_dir = "F:\\songs"
        songs = os.listdir(music_dir)
        print(songs)    
        random = os.startfile(os.path.join(music_dir, songs[1]))
    elif "nihal" in query:         
        v.speak("Nihal 2 point o in your service Mister")
        st.write("Nihal 2 point o in your service Mister")
        v.speak("How can i help you")
    elif 'exit' in query or 'close' in query:
        v.speak("Nihal 2 point o sighning off ")
        v.speak("Thanks for giving me your time")
        break 
    else:
        response= get_gemini_response(query)
        st.subheader("The response is")
        st.write(response)
        v.speak(response)




# if submit:
#     st.write(f'Hello {name}\n This is your output')
#     # st.write(f'Since it is for {reason} purpose we are allowing your request')
#     response=get_gemini_response(input)
#     st.subheader("The response is")
#     st.write(response)

# to run -> streamlit run c:/Users/jerri/OneDrive/Documents/AI_ML/simple_GenAI/app.py
# to create environment -> conda create -n {name}

#background change to image
# def set_bg_hack(main_bg):
#     """
#     A function to set a background image for the main panel in Streamlit.

#     Args:
#         main_bg: The path to the background image file.
#     """
#     main_bg_ext = "jpeg"  # Replace with the actual extension of your image file

#     # Encode the image as a base64 string
#     with open(main_bg, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()

#     # Set the background image using CSS
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/{main_bg_ext};base64,{encoded_string});
#             background-size: cover; 
            
#         }}
#         </style>
        
#         """,
#         unsafe_allow_html=True,
#     )


# # Path to your background image
# background_img = r"C:\Users\jerri\Downloads\jaggu.jpeg" 

# # Set the background image
# set_bg_hack(background_img)
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