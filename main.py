import argparse
from caesar_cipher import encrypt_caesar, decrypt_caesar
from morse import encrypt_morse, decrypt_morse

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt messages using Caesar cipher or Morse code.\n\n"
                    "Examples:\n"
                    "  python main.py -m -e input.txt output.txt   # Encrypt with Morse code\n"
                    "  python main.py -m -d input.txt output.txt   # Decrypt Morse code\n"
                    "  python main.py -c -e -n 3 input.txt output.txt   # Encrypt Caesar with shift 3\n"
                    "  python main.py -c -d -n 3 input.txt output.txt   # Decrypt Caesar with shift 3",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('-c', action='store_true', help='Use Caesar cipher')
    parser.add_argument('-m', action='store_true', help='Use Morse code')
    parser.add_argument('-e', action='store_true', help='Encrypt the message')
    parser.add_argument('-d', action='store_true', help='Decrypt the message')
    parser.add_argument('-n', type=int, help='Shift for Caesar cipher (required with -c)')
    parser.add_argument('input_file', help='Path to input file')
    parser.add_argument('output_file', help='Path to output file')

    args = parser.parse_args()

    text = read_file(args.input_file)

    if args.e:
        if args.c:
            if args.n is None:
                print("Error: Shift (-n) is required for Caesar cipher.")
                return
            result = encrypt_caesar(text, args.n)
        elif args.m:
            result = encrypt_morse(text)
            if result.startswith("Error:"):
                print(result)
                return
        else:
            print("Error: You must specify either -c (Caesar) or -m (Morse).")
            return
    elif args.d:
        if args.c:
            if args.n is None:
                print("Error: Shift (-n) is required for Caesar cipher.")
                return
            result = decrypt_caesar(text, args.n)
        elif args.m:
            result = decrypt_morse(text)
        else:
            print("Error: You must specify either -c (Caesar) or -m (Morse).")
            return
    else:
        print("Error: You must specify -e (encrypt) or -d (decrypt).")
        return

    write_file(args.output_file, result)

if __name__ == '__main__':
    main()
