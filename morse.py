# Morse code dictionary: maps letters and numbers to Morse
MORSE_CODE_DICT = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',
    'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',   'J': '.---',
    'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',   'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----','2': '..---','3': '...--','4': '....-','5': '.....',
    '6': '-....','7': '--...','8': '---..','9': '----.','0': '-----',
    ' ': '/'
}

def encrypt_morse(text):
    text = text.upper()
    result = ""

    if all(char in ".-/ " for char in text):
        return "Error: Input seems to already be in Morse code."

    for letter in text:
        if letter in MORSE_CODE_DICT:
            morse = MORSE_CODE_DICT[letter]
            result += morse + " "
        else:
            continue

    return result.strip()

def decrypt_morse(morse_text):
    MORSE_TO_LETTER = {}
    for letter in MORSE_CODE_DICT:
        morse = MORSE_CODE_DICT[letter]
        MORSE_TO_LETTER[morse] = letter

    result = ""
    parts = morse_text.strip().split(" ")

    for code in parts:
        if code in MORSE_TO_LETTER:
            result += MORSE_TO_LETTER[code]
        else:
            continue

    return result
