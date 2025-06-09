import pyttsx3

engine = pyttsx3.init()


text = "This is text only number. I cannot accept calls. Please text to me only."
engine.setProperty("rate", 100)
engine.save_to_file(text, "textonly.mp3")
engine.runAndWait()

