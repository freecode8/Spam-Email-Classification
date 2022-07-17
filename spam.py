import pickle
import streamlit as st
import numpy as np
from win32com.client import Dispatch

def speak(text):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.speak(text)

classifier = pickle.load(open('spam.pkl' , 'rb'))

# classifier = pickle.load('spam.pkl', 'rb')


def main():
    st.title(" Email Spam Classification ")
    st.write("Build with streamlit & phyton ")
    msg = st.text_input("Enter a text :")
    if st.button("Predict"):
        word_dict_pickle = open("word_pickle.pkl", 'rb')
        word_dict = pickle.load(word_dict_pickle)
        word_dict_pickle.close()

        sample=[]

        for i in word_dict:
            sample.append(msg.split(" ").count(i[0]))

        sample = np.array(sample)

        pred = classifier.predict(sample.reshape(1,3000))
        result = pred[0]


        if result == 1:
            st.error(" This is a spam mail")
            speak("text is spam mail")
        else:
            st.error("this is a ham mail")
            speak("text is ham mail")


main()
