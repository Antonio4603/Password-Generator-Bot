"""
Modulo per la logica di generazione password e cifratura.

Questo modulo fornisce utility per la creazione di password sicure,
generazione di PIN numerici, verifica della robustezza e cifratura base.
"""
import secrets
import string


def generate_password(num_words: int = 4) -> str:
    """
    Genera una password composta da parole casuali separate da trattini.

    Args:
        num_words (int): Il numero di parole da includere. Minimo 4.

    Returns:
        str: La password generata (es. 'mela-libro-fiume-razzo').

    Raises:
        ValueError: Se num_words è inferiore a 4.
    """
    if num_words < 4:
        raise ValueError("La lunghezza minima è 4 parole.")

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
    """
    Verifica se una password rispetta i criteri minimi di sicurezza.

    Criteri:
    - Almeno 15 caratteri
    - Almeno un numero
    - Almeno una maiuscola
    - Almeno un simbolo di punteggiatura
    """
    is_long_enough = len(password) >= 15
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    return is_long_enough and has_digit and has_upper and has_symbol
    
def generate_pin(length: int = 4) -> str:
    """
    Genera un PIN numerico casuale della lunghezza specificata.
    """
    result = ""
    for _ in range(length):
        digit = secrets.choice(string.digits)
        result = result + digit
    return result    