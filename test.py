import pyttsx3

engine = pyttsx3.init()


text = "Python is a great programming language. Fuck you Cock Dick Penis Sucker"
engine.setProperty("rate", 100)
engine.save_to_file(text, "test.mp3")
engine.runAndWait()

