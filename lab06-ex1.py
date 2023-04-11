from gtts import gTTS

from googletrans import Translator
import streamlit as st

translator = Translator()
word = st.text_input('Type some text:')
language=st.text_input('Type in a language')
translation=translator.translate(word,dest=language)


tts1=gTTS(text=translation.text, lang=language) 
tts1.save('user.mp3')

print('auf Ru:')
st.audio('user.mp3')
