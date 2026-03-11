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