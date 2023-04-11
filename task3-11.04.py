from gtts import gTTS
import IPython.display as ipd  
from googletrans import Translator

translator = Translator()
word = st.texct_input('Type some text:')

languageis = translator.translate(word, dest='ru') #---> lingua che viene tradotta da un'altra lingua

tts1=gTTS(text=languageis.text, lang='ru') #--> lingua pronunciata
tts1.save('user.mp3')

print('auf Ru:')
st.audio('user.mp3')
