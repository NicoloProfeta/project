import streamlit as st
from gingerit.gingerit import GingerIt
import pyttsx3
import language_tool_python
from gtts import gTTS

def correct_german_text(text):
    #parser = GingerIt()
    #corrected = parser.parse(text)['result']
    #return corrected
    tool = language_tool_python.LanguageToolPublicAPI('de-DE')
    return tool.correct(text)
    

def speak_german_text(mytext):
    tts1=gTTS(text="Der Tisch ist neu", lang="de")
    tts1.save('file.mp3')
    audio_file = open("file.mp3", "rb")
    st.audio(data=audio_file, format="audio/mp3", start_time=0)
    #engine = pyttsx3.init()
    #engine.setProperty('rate', 150)
    #engine.setProperty('voice', 'german')
    #engine.say(text)
    #engine.say("Der Tisch ist gelb")
    #engine.runAndWait()

def main():
    st.title("Deutscher Textkorrektor")
    user_input = st.text_area("Geben Sie Ihren Text auf Deutsch ein:", max_chars=500)
    
    if st.button("Korrektur durchführen"):
        if len(user_input) > 0:
            if len(user_input) > 500:
                st.error("Der Text darf maximal 500 Zeichen lang sein.")
            else:
                corrected_text = correct_german_text(user_input)
                st.success("Korrigierter Text:")
                st.write(corrected_text)
                st.subheader("Hören Sie sich die richtige deutsche Aussprache an:")
                st.button("Aussprache abspielen", on_click=lambda: speak_german_text(corrected_text))

if __name__ == "__main__":
    main()
