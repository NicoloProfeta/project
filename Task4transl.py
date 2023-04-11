
import json, requests
from googletrans import Translator
import streamlit as st

language = st.selectbox('Please, select a destination language', ('it', 'de', 'en', 'ru'))
keyword = st.text_input('insert a  word')
translator = Translator()

if (language and keyword):
  translate = translator.translate(keyword, dest=language)
  st.write(translate.text)
