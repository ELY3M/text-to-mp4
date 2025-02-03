import pyttsx3

engine = pyttsx3.init()


text = "This is text only number. I cannot accept calls because I cant hear and talk. Please email or text to me only."
engine.setProperty("rate", 100)
engine.save_to_file(text, "textemailonly.mp3")
engine.runAndWait()

