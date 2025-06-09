import pyttsx3

engine = pyttsx3.init()


text = "FUCK YOU FOR CALLING ME!  Eat a penis and do not call me. I HATE ALL CALLS! ALL NUMBERS THAT CALLED THIS NUMBER WILL BE BLOCKED ON ALL OF MY NUMBERS! AND REPORTED TO FBI & FCC! YOU WILL BE ARRESTED!"
engine.setProperty("rate", 100)
engine.save_to_file(text, "fuckcalls.mp3")
engine.runAndWait()

