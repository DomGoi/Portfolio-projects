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

# Example usage
morse_code_path = get_resource_path('morse_code.txt')
numbers_path = get_resource_path('numbers.txt')
special_path = get_resource_path('special.txt')

# Now you can open these files
with open(morse_code_path, 'r') as f:
    morse_code_data = f.read()

with open(numbers_path, 'r') as f:
    numbers_data = f.read()

with open(special_path, 'r') as f:
    special_data = f.read()

class Code():
    def __init__(self):
        self.WHITE="#FFFFFF"
        self.GREY="#C0C0C0"
        self.window_1 = Toplevel()

        self.window_1.title("Morse Coder")
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

        label = Label(self.window_1, text="Please input message you want to code.", bg=self.GREY, font=('Arial', 25,'bold'))
        label.grid(column=1, row=0,pady=20, padx=10)

        self.text_box=Text(self.window_1, padx=10, pady=20, insertborderwidth=10)
        self.text_box.grid(column=0,row=2, columnspan=4, rowspan=2)

        button_upload = Button(self.window_1, text="Upload the file (.txt)", width=20, height=2,
                               font=("Arial", 15, "bold"),
                               command=self.upload_file)
        button_upload.grid(column=1, row=4, pady=20, padx=10)

        button_close = Button(self.window_1, text="Quit", width=20, height=2, font=("Arial", 15, "bold"),
                              command=lambda: self.close_window(self.window_1))
        button_close.grid(column=0, row=4, pady=20, padx=10)

        button_code = Button(self.window_1, text="Code", width=20, height=2, font=("Arial", 15, "bold"),
                               command=self.code)
        button_code.grid(column=2, row=4, pady=20, padx=10)

        # Start the main loop for this window
        self.window_1.mainloop()

    def close_window(self, window):
        window.destroy()

    def import_letters(self, filename, split_char=None):
        try:
            filename = get_resource_path(filename)
            with open(filename, 'r') as file:
                content = file.read()
                if split_char:
                    return ast.literal_eval(content.split('=')[1].strip())
                return ast.literal_eval(content)

        except Exception as e:
            print(f"Error reading the text file {filename}: {e}")
            return {}

    def code(self):
        self.morse_dict = self.import_letters('morse_code.txt', '=')
        self.morse_num = self.import_letters('numbers.txt', '=')
        self.morse_special = self.import_letters('special.txt')

        self.message = self.text_box.get("1.0", END)
        self.message_to_code = self.message.strip().upper()
        self.coded_message = []

        for n in self.message_to_code:
            if n in self.morse_dict:
                self.coded_message.append(self.morse_dict[n] + ' ')
            elif n in self.morse_num:
                self.coded_message.append(self.morse_num[n] + ' ')
            elif n in self.morse_special:
                self.coded_message.append(self.morse_special[n] + ' ')
            elif n == ' ':
                self.coded_message.append('/')
            else:
                self.coded_message.append(n)

        self.result = ''.join(self.coded_message)
        self.show_result(self.result)

    def save_output(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            with open(filename, 'w') as file:
                file.write(self.result)
                messagebox.showinfo("File saved", f"Output saved successfully as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

    def show_result(self, result):

        self.window_2 = Toplevel(self.window_1)
        self.window_2.title("Morse code message")
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

        self.label_result = Label(self.frame_2, padx=20, pady=20, text="Your message in morse code:", bg=self.GREY,
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
        save_result_button.grid(column=4, row=6, pady=20, padx=10)

        self.frame_2.update_idletasks()
        self.canvas_2.configure(scrollregion=self.canvas_2.bbox("all"))

        self.window_2.grid_rowconfigure(0, weight=1)
        self.window_2.grid_columnconfigure(0, weight=1)


