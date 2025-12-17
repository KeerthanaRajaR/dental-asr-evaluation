import pyttsx3
from pathlib import Path

engine = pyttsx3.init()
engine.setProperty('rate', 170)

text = Path("conversations/convo2_reference.txt").read_text()
engine.save_to_file(text, "audio/convo2.wav")
engine.runAndWait()
