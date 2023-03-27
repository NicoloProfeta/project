import streamlit as st
city = st.radio("What's your favorite city?",('Bolzano', 'Bonn', 'Barcelona'))
if city == 'Bolzano':
     st.write('You selected Bolzano.')
else:
     st.write("You did not select Bolzano")
