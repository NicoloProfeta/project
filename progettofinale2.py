import streamlit as st
from gingerit.gingerit import GingerIt
import pyttsx3
import language_tool

def correct_german_text(text):
    #parser = GingerIt()
    #corrected = parser.parse(text)['result']
    #return corrected
    language_tool_python.LanguageToolPublicAPI('de')
    return tool.correct(text)
    

def speak_german_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('voice', 'german')
    engine.say(text)
    engine.runAndWait()

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
