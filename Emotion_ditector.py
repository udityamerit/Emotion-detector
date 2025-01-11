import cv2
import numpy as np
from fer import FER
import streamlit as st

emotion_model = FER(mtcnn=True)

def predict_emotion(image):
    emotions = emotion_model.top_emotion(image)
    return emotions[0] if emotions else "Unknown"

def main():
    st.title("Guess the Emotion Game 🎮")
    st.write("Guess the emotion in the image and test your skills against AI!")

   
    user_guess = st.text_input("Your Guess (happy, sad, angry, surprise, neutral):")
    
    st.write("Capture your emotion:")
    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer:
        file_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        st.image(img, caption="Your Image", use_container_width=True)  
        predicted_emotion = predict_emotion(img)

        if user_guess.lower() == predicted_emotion:
            st.success(f"Correct! The emotion is {predicted_emotion} 🎉")
        else:
            st.error(f"Oops! The emotion is actually {predicted_emotion} 😞")
        st.write("Keep trying!")

if __name__ == "__main__":
    main()
