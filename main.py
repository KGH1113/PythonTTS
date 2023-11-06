import tkinter as tk
from gtts import gTTS
import pygame
from io import BytesIO

# Initialize pygame mixer
pygame.mixer.init()

# Create a function to handle the TTS process
def text_to_speech():
    text = text_entry.get()
    
    if text:
        # Create a gTTS object with the Korean language code 'ko' for Korean
        tts = gTTS(text, lang='ko')
        
        # Save the speech as an in-memory audio file
        audio_file = BytesIO()
        tts.write_to_fp(audio_file)
        
        # Play the audio from the in-memory file
        audio_file.seek(0)
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

# Create the main application window
app = tk.Tk()
app.title("Text-to-Speech Program (Korean)")

# Adjust window size
app.geometry("400x400")

# Create Label
label = tk.Label(app, text="안내맨트를 입력하세요:", width=25, height=5, relief="solid")
label.pack()

# Create and configure a text entry field
text_entry = tk.Entry(app, width=50)
text_entry.pack(pady=10)

# Create a button to trigger the TTS function
tts_button = tk.Button(app, text="Convert to Speech", command=text_to_speech)
tts_button.pack()

# Start the main loop
app.mainloop()
