import pyttsx3
engine=pyttsx3.init()
#speeed of the robot voice
engine.setProperty("rate",150)
#the robot volume value(0-1)
engine.setProperty("volume",0.8)
#what it say
engine.say("aswin anand and shashank are good boy's")
engine.runAndWait()
