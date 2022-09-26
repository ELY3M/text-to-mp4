import pyttsx3

engine = pyttsx3.init()


text = "Fuck you Cock Dick Penis Sucker. Please suck my wet penis"
engine.setProperty("rate", 100)
engine.save_to_file(text, "fuck.mp3")
engine.runAndWait()

