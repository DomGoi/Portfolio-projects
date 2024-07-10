from tkinter import *
from tkinter import filedialog, messagebox
import ast
import os
import sys

def get_resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Decode():
    def __init__(self):
        self.WHITE = "#FFFFFF"
        self.GREY = "#C0C0C0"
        self.window_1 = Toplevel()

        self.window_1.title("Morse Decoder")
        self.window_1.minsize(400, 600)
        self.window_1.config(pady=20, padx=20, bg=self.GREY)

        self.setup_ui()

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.morse_code_content = file.read()
                self.text_box.delete(1.0, END)
                self.text_box.insert(END, self.morse_code_content)

    def setup_ui(self):
        label = Label(self.window_1, text="Please input morse code message (space between characters, '/' between words, '-' for dash) or upload it.", font=("Arial", 14, "bold"), bg=self.GREY)
        label.grid(column=0, row=0, columnspan=3, pady=20, padx=10)

        self.text_box = Text(self.window_1, padx=10, pady=20, insertborderwidth=10)
        self.text_box.grid(column=0, row=1, columnspan=3, pady=10, padx=10)

        button_upload = Button(self.window_1, text="Upload the file (.txt)", width=20, height=2, font=("Arial", 15, "bold"),
                               command=self.upload_file)
        button_upload.grid(column=1, row=4, pady=20, padx=10)

        button_close = Button(self.window_1, text="Close the window", width=20, height=2, font=("Arial", 15, "bold"), command=self.close_window)
        button_close.grid(column=2, row=4, pady=20, padx=10)

        button_decode = Button(self.window_1, text="Decode", width=20, height=2, font=("Arial", 15, "bold"), command=self.decode)
        button_decode.grid(column=0, row=4, pady=20, padx=10)

    def close_window(self, window=None):
        if window:
            window.destroy()
        else:
            self.window_1.destroy()

    def import_letters(self, filename, separator=None):
        try:
            filename = get_resource_path(filename)
            with open(filename, 'r') as file:
                content = file.read()
                if separator:
                    return ast.literal_eval(content.split('=')[1].strip())
                return ast.literal_eval(content)
        except Exception as e:
            print(f"Error reading the text file {filename}: {e}")
            return {}

    def decode(self):
        self.morse_dict = self.import_letters('morse_code.txt', '=')
        self.morse_dict_inv = {v: k for k, v in self.morse_dict.items()}
        self.morse_num = self.import_letters('numbers.txt', '=')
        self.morse_num_inv = {v: k for k, v in self.morse_num.items()}
        self.morse_special = self.import_letters('special.txt')
        self.morse_special_inv = {v: k for k, v in self.morse_special.items()}

        self.message_to_decode = self.text_box.get("1.0", END).strip()

        decoded_message = ""
        morse_words = self.message_to_decode.split('/')
        for word in morse_words:
            morse_chars = word.strip().split(' ')
            for morse_char in morse_chars:
                if morse_char in self.morse_dict_inv:
                    decoded_message += self.morse_dict_inv[morse_char]
                elif morse_char in self.morse_num_inv:
                    decoded_message += self.morse_num_inv[morse_char]
                elif morse_char in self.morse_special_inv:
                    decoded_message += self.morse_special_inv[morse_char]
                else:
                    decoded_message += f'{morse_char}'
            decoded_message += ' '
        self.text_res=decoded_message.strip()
        self.show_result(self.text_res)


    def save_output(self):
        try:
            filename=filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            with open(filename, 'w') as file:
                file.write(self.text_res)
                messagebox.showinfo("File saved", f"Output saved successfully as {filename}")
        except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def show_result(self, result):
        self.window_2 = Toplevel(self.window_1)
        self.window_2.title("Decoded Morse Code Message")
        self.window_2.config(pady=20, padx=20, bg=self.GREY)

        self.canvas_2 = Canvas(self.window_2, bg=self.GREY, width=1000, height=600)
        self.canvas_2.grid(row=0, column=0, sticky="nsew")

        scrollbar = Scrollbar(self.window_2, orient=VERTICAL, command=self.canvas_2.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.canvas_2.configure(yscrollcommand=scrollbar.set)

        self.frame_2 = Frame(self.canvas_2, bg=self.GREY)
        self.canvas_2.create_window((0, 0), window=self.frame_2, anchor='nw')

        self.label_res = Label(self.frame_2, padx=20, pady=20, text="Your input message was:", bg=self.GREY,
                               font=('Arial', 20, "bold"))
        self.label_res.grid(column=1, row=0, padx=10, pady=20)

        input_text = Text(self.frame_2, padx=10, pady=20, height=10, width=50)
        input_text.insert(END, self.text_box.get("1.0", END))
        input_text.config(state=DISABLED)
        input_text.grid(column=0, row=1, columnspan=3, rowspan=2, pady=20, padx=10)

        self.label_result = Label(self.frame_2, padx=20, pady=20, text="Decoded message:", bg=self.GREY,
                                  font=('Arial', 20, "bold"))
        self.label_result.grid(column=1, row=4, padx=10, pady=20)

        result_text = Text(self.frame_2, padx=10, pady=20, insertborderwidth=10)
        result_text.insert(END, result)
        result_text.config(state=DISABLED)
        result_text.grid(column=0, row=5, columnspan=3, rowspan=1, pady=20, padx=10)

        close_result_button = Button(self.frame_2, text="Close", width=20, height=2, font=("Arial", 15, "bold"),
                                     command=lambda: self.close_window(self.window_2))
        close_result_button.grid(column=0, row=6, pady=20, padx=10)

        save_result_button = Button(self.frame_2, text="Export to txt", width=20, height=2, font=("Arial", 15, "bold"),
                                    command=self.save_output)
        save_result_button.grid(column=2, row=6, pady=20, padx=10)

        self.frame_2.update_idletasks()
        self.canvas_2.configure(scrollregion=self.canvas_2.bbox("all"))

        self.window_2.grid_rowconfigure(0, weight=1)
        self.window_2.grid_columnconfigure(0, weight=1)

