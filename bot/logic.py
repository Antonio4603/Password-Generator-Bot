import secrets
import string

def generate_password(num_words: int = 4) -> str:
    if num_words < 4:
        raise ValueError("La lunghezza minima deve essere di 4 parole.")

    word_list = [
        "aiuola", "mela", "nuvola", "tastiera",
        "fiume", "scoglio", "razzo", "libro"
    ]

    words = []
    for _ in range(num_words):
        word = secrets.choice(word_list)
        words.append(word)

    return "-".join(words)


def is_strong_password(password: str) -> bool:
    is_long_enough = len(password) >= 15
    has_digit = False
    has_upper = False
    has_symbol = False

    for c in password:
        if c.isdigit():
            has_digit = True
        if c.isupper():
            has_upper = True
        if c in string.punctuation:
            has_symbol = True

    return is_long_enough and has_digit and has_upper and has_symbol

def generate_pin(length: int=4) -> str:
    result=""
    for _ in range(length):
        digit=secrets.choice(string.digits)
        result=result+digit
    return result

def cesar_cipher(text: str, shift: int=3) -> str:
    result=""
    for char in text:
        if char.isalpha():
            start=ord('a') if char.islower() else ord('A')
            result+=chr((ord(char)-start+shift)%26+start)
        elif char.isdigit():
            result+=chr((ord(char)-ord('0')+shift)%10+ord('0'))
        else:
            result+=char
    return result
