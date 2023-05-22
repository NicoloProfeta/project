import streamlit as st
import grammarbot
from gtts import gTTS
from io import BytesIO
import base64

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
    st.title("Peer Review - DEUTSCH")
    st.write("Schreib bitte deinen Text (500 Wörter oder weniger):")

    # Create a text input box for the user to enter the text
    text = st.text_area("Tipp deinen Text", height=200)

    # Check if text exceeds the length limit
    if len(text) > 500:
        st.error("Dein Text ist zu lang! Versuch es noch einmal!")
        return

    if st.button("Revise Homework"):
        revised_text = revise_homework(text)
        st.write("\nRevised Homework:")
        st.write(revised_text)

    if st.button("Hör die richtige Aussprache!"):
        if "revised_text" in locals():
            audio = generate_pronunciation(revised_text)
            audio_bytes = audio.read()
            st.audio(audio_bytes, format='audio/mp3')
        else:
            st.warning("Überprüfe bitte deinen Text vorm Hören!.")

if __name__ == "__main__":
    main()

