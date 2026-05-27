from string import ascii_lowercase, ascii_uppercase, punctuation, whitespace, digits

def main():

    try :
        text = input()
        while text:
            print(f"The text contains {len(text)} characters:")
            print(f"{len([c for c in text if c in ascii_uppercase])} upper letters")
            print(f"{len([c for c in text if c in ascii_lowercase])} lower letters")
            print(f"{len([c for c in text if c in punctuation])} punctuation marks")
            print(f"{len([c for c in text if c in whitespace])} spaces")
            print(f"{len([c for c in text if c in digits])} digits")
            text = input()
    except KeyboardInterrupt or EOFError as error:
        pass

if __name__ == "__main__":
    main()
