import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

engine.say("Olá, meu nome é Eva. Esse é um teste de voz")
engine.runAndWait()