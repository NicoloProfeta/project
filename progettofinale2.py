import streamlit as st
import grammarbot
from gtts import gTTS
from io import BytesIO

def revise_homework(text):
    # Use GrammarBot to correct orthography
    tool = grammarbot.LanguageTool('de-DE')
    matches = tool.check(text)
    revised_text = grammarbot.correct(text, matches)
    return revised_text

def generate_pronunciation(text):
    # Generate pronunciation audio using gTTS
    tts = gTTS(text, lang='de')
    audio = BytesIO()
    tts.save(audio)
    return audio

def main():
    st.title("Homework Revision Program (German)")
    st.write("Please enter your text (500 characters or less):")

    # Create a text input box for the user to enter the text
    text = st.text_area("Enter your text", height=200)

    # Check if text exceeds the length limit
    if len(text) > 500:
        st.error("Text exceeds the length limit of 500 characters. Please try again.")
        return

    if st.button("Revise Homework"):
        revised_text = revise_homework(text)
        st.write("\nRevised Homework:")
        st.write(revised_text)

    if st.button("Hear Pronunciation"):
        if "revised_text" in locals():
            audio = generate_pronunciation(revised_text)
            st.audio(audio.read(), format='audio/mp3')
        else:
            st.warning("Please revise the homework before hearing the pronunciation.")

if __name__ == "__main__":
    main()
