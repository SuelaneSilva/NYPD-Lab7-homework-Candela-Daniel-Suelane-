def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = 65
            else:
                base = 97

            position = ord(char) - base
            new_position = (position + shift) % 26
            new_char = chr(new_position + base)

            result += new_char
        else:
            result += char

    return result

def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)
