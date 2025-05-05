
# 🔐 Encryption/Decryption Tool

This is a group project to build a simple command-line tool that can **encrypt** or **decrypt** messages from text files using **Caesar cipher** or **Morse code**.

---

## 📌 Description

The program reads a message from an input file, encrypts or decrypts it using the selected method, and writes the result to an output file.

You can choose between:
- **Caesar cipher** (with a custom right shift)
- **Morse code**

---

## 🚀 How to Use

Run the tool from the terminal:

```bash
python main.py -h
```
This will show a help message with usage instructions.

## 📂 Project Structure

```
project/
├── caesar_cipher.py     # Caesar cipher logic
├── morse.py             # Morse code logic
├── main.py              # Command-line interface and file I/O
├── participants.txt     # List of participants
├── input.txt            # Example input file
├── output.txt           # Output file (result goes here)
└── README.md            # This documentation
```
