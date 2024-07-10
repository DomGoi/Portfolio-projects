Morse (De)coder

This is my first independently made PyCharm project, which I further exported into a functional executable file.
Description

This program allows any user to encode their own unique message into Morse code using international Morse code (letters, numbers, and special signs). Messages can be uploaded from a .txt file for both the encoding and decoding functions. Additionally, the obtained message, either coded or decoded, can be saved in a desired file in .txt format.
Features

    Encode text to Morse code.
    Decode Morse code to text.
    Upload messages from a .txt file for encoding or decoding.
    Save the encoded or decoded message to a .txt file.

Installation

To run the program as an executable, simply download and run the provided executable file.

If you prefer to run the source code, follow these steps:

    Clone the repository:

    bash

git clone https://github.com/yourusername/morse-decoder.git
cd morse-decoder

Install the required packages:

This project requires Python 3.x. Install the dependencies with:

bash

pip install -r requirements.txt

Run the application:

bash

    python main.py

Usage

    Open the application.
    Choose to encode or decode a message.
    Input your message directly or upload a .txt file containing the message.
    Click the corresponding button to encode or decode the message.
    Optionally, save the result to a .txt file.

File Structure

css

morse_code_project/
├── main.py
├── coder.py
├── decoder.py
├── morse_code.txt
├── numbers.txt
├── special.txt
├── requirements.txt
└── README.md

    main.py: Main menu and interface.
    coder.py: Encoding functions.
    decoder.py: Decoding functions.
    morse_code.txt: Morse code mapping for letters.
    numbers.txt: Morse code mapping for numbers.
    special.txt: Morse code mapping for special characters.
    requirements.txt: List of dependencies.
    README.md: This file.

Building the Executable

To build the executable file, you can use PyInstaller:

    Install PyInstaller:

    bash

pip install pyinstaller

Create the executable:

bash

pyinstaller --onefile --windowed main.py

Include additional files:

Modify the .spec file created by PyInstaller to include your text files:

python

# main.spec
a = Analysis(['main.py'],
             pathex=['/path/to/your/project'],
             binaries=[],
             datas=[('morse_code.txt', '.'), ('numbers.txt', '.'), ('special.txt', '.')],  # Include your files here
             ...

Build with the spec file:

bash

    pyinstaller main.spec

Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

Thanks to all who provided guidance and support in creating this project.
