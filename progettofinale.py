import requests
import json

import streamlit as st

APIkey = "09972ee78cmsh877ccbbcbd94f02p13fc75jsn53d32a153331"
Text = st.text_input("Schreib deinen Text")
url = "https://grammarbot-neural.p.rapidapi.com/v1/check" + Text + '&appid=' + APIkey
print(url)

response = requests.get(url)
grammarbot = json.loads(response.text)

