from gtts import gTTS
import os

mytext = input("Type what I have to say:")
language = 'en'
myfile = gTTS(text=mytext, lang=language, slow=False)
filename = input("Enter a file name for your audio file:")
myfile.save(filename+".mp3")

os.system(filename+".mp3")
