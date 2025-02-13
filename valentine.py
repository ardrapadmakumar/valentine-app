import streamlit as st
import os
import base64

# Set up page configuration
st.set_page_config(page_title="Valentine's Surprise", page_icon="❤️", layout="wide")

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to encode an image as base64
def get_base64_image(image_path):
    if not os.path.exists(image_path):  # Check if file exists
        st.error("Image not found! Check the file path.")
        return ""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Function to apply background image
def set_background(image_path):
    base64_img = get_base64_image(image_path)
    if base64_img:  # Apply only if image is found
        page_bg_img = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{base64_img}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to navigate pages
def switch_to_love_letter():
    st.session_state.page = "love_letter"
    st.rerun()

# Home Page
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align: center;'>Would you be my Valentine? ❤️</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])  # Centering the button
    
    with col2:
        if st.button("Yesss 💖", use_container_width=True):
            switch_to_love_letter()  
        
        if st.button("No💔", use_container_width=True):
            st.error("Whyyyy Nottt???!!!💔")

# Love Letter Page (with background image)
elif st.session_state.page == "love_letter":
    set_background("catvector.jpeg")    
    
    st.markdown("<h1 style='text-align: center; color: white;'>Wellll, so you chose yes?? ❤️</h1>", unsafe_allow_html=True)
    
    st.markdown(
    """
    <div style="text-align: center;">
        <h2>Happy Valentine's Day, baby.</h2>
        <p1 style="font-size: 15px;">Since you chose yes here's a lil gift for ya 😃👌🏼⬇️ </p1>
    </div>
    """,
    unsafe_allow_html=True
)
    st.write("\n\n\n\n") 
    st.write("\n\n\n\n")
    col5, col6, col7, col8, col9, col10, col11 = st.columns([1, 2, 3, 4, 3, 2, 1])

    with col8:
        with open("eatkids.png", "rb") as file:
            btn = st.download_button(
                label="freaky pics 🤤",
                data=file,
                file_name="eatkids.png",
                mime="image/png",
            )
    st.write("\n\n\n") 
    st.write("\n\n\n") 

    col10, col11, col12 = st.columns([1, 2, 1])

    with col10:
        if st.button("Home page??"):
            st.session_state.page = "home"