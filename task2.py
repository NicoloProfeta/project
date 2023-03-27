# ! python3
import json, requests 
import streamlit as st

# add your own APIkey
APIkey = "081fb9648932cba5507ccd0e1c6e0e09"
location = st.text_input("Enter your city:")

if location:
# check API documentation to see what structure of URL is needed to access the data
# http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
  url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey
# print(url)


# Download the JSON data from OpenWeatherMap.org's API.
  response = requests.get(url)  
# Uncomment to see the raw JSON text:
# print(response.text)  


# Load JSON data into a Python variable.
  weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
# print(weatherData) 
# from pprint import pprint 
# pprint(weatherData) 

  print(weatherData['main']['temp_min'])
  print(weatherData['main']['temp_max'])
  print(weatherData['weather'][0]['description'])

  st.header("Weather forecast")
  st.write("Temperature: ", weatherData['main']['temp_max'], " °C")
