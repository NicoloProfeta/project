from gtts import gTTS
import IPython.audio as ipd  
from googletrans import Translator

translator = Translator()
word = st.texct_input('Type some text:')

languageis = translator.translate(word, dest='ru') 

tts1=gTTS(text=languageis.text, lang='ru') 
tts1.save('user.mp3')

print('auf Ru:')
st.audio('user.mp3')
