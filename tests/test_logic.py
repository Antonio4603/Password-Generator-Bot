"""
Modulo di test per la logica del Password Generator Bot.
Questo modulo contiene i test unitari per la generazione di password,
PIN e cifratura di Cesare.
"""
import pytest

from bot.logic import (cesar_cipher, generate_password, generate_pin,
                       is_strong_password)


def test_generate_password_count() -> None:
    """Verifica che il numero di parole generate sia esattamente quello richiesto."""
    num_expected = 10
    pwd = generate_password(num_expected)
    assert len(pwd.split("-")) == num_expected


def test_generate_password_min_length() -> None:
    """Verifica che venga sollevata un'eccezione per lunghezze inferiori a 4."""
    with pytest.raises(ValueError):
        generate_password(3)
