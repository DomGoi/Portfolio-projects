import sys
import os
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from code import Code
from decode import Decode

BLACK = "#000000"
WHITE = "#FFFFFF"

# Determine the base path for accessing resources depending on whether it's a script or a bundled application
if getattr(sys, 'frozen', False):
    # Running as bundled executable (PyInstaller)
    base_path = sys._MEIPASS  # Use this attribute to get the base path
else:
    # Running as a script
    base_path = os.path.abspath(os.path.dirname(__file__))  # Use the current directory

# Example of accessing a file within the application's directory
image_path = os.path.join(base_path, 'morse-code_5940809.png')

# Initialize the main window
window = Tk()
window.title("Morse (De)Coder")
window.minsize(400, 600)
window.config(pady=20, padx=20, bg=WHITE)

# Font
custom_font = font.Font(family="Times")

# Image
image = Image.open(image_path)
background_image = ImageTk.PhotoImage(image)

# Canvas
canvas = Canvas(window, width=image.width, height=image.height, highlightthickness=0, bg=WHITE)
canvas.create_image(0, 40, image=background_image, anchor=NW)
canvas.grid(column=0, row=1, columnspan=3, rowspan=3)

title_text = canvas.create_text(image.width // 2, 20, text="Morse (De)Coder", fill="black", font=(custom_font, 25, "bold"))

# Code Button
def code_action():
    Code()

button_code = Button(window, text="Code", width=20, height=2, fg=BLACK, font=("Arial", 15, "bold"), command=code_action)
button_code.grid(column=0, row=4, pady=20, padx=10)

# Decode Button
def decode_action():
    Decode()

button_decode = Button(window, text="Decode", width=20, height=2, font=("Arial", 15, "bold"), command=decode_action)
button_decode.grid(column=2, row=4, pady=20, padx=10)

window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

window.mainloop()
