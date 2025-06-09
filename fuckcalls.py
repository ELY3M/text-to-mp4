import pyttsx3

engine = pyttsx3.init()


text = "FUCK YOU!!!!  FUCK YOU!!!!  FUCK YOU!!!!  DO NOT CALL ME!  FUCK YOU!!! AND EAT YOUR PENIS SPAMMERS!!!  FUCK OFF!!!  ALL NUMBERS THAT CALLED ME WILL BE REPORTED TO FCC AND FBI AND BLOCKED!!!  GO AWAY!"
engine.setProperty("rate", 100)
engine.save_to_file(text, "fuckcalls.mp3")
engine.runAndWait()

