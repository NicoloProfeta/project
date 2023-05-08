from grammarbot import GrammarBotClient
import requests
import json

import streamlit as st

client = GrammarBotClient()

APIkey = "09972ee78cmsh877ccbbcbd94f02p13fc75jsn53d32a153331"
client = GrammarBotClient(api_key='APIkey')
Text = st.text_input("Schreib deinen Text")
url = "https://grammarbot-neural.p.rapidapi.com/v1/check" + Text + '&appid=' + APIkey
#print(url)

res = client.check(Text)

st.write(res)


