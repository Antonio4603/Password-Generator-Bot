"""
Modulo di test per la logica del Password Generator Bot.
Questo modulo contiene i test unitari per la generazione di password,
PIN e cifratura di Cesare.
"""

import pytest

from bot.logic import cesar_cipher, generate_password, generate_pin, is_strong_password


def test_generate_password_count() -> None:
    """Verifica che il numero di parole generate sia esattamente quello richiesto."""
    num_expected = 10
    pwd = generate_password(num_expected)
    assert len(pwd.split("-")) == num_expected


def test_generate_password_min_length() -> None:
    """Verifica che venga sollevata un'eccezione per lunghezze inferiori a 4."""
    with pytest.raises(ValueError):
        generate_password(3)


def test_is_strong_password_true() -> None:
    """Testa una password che soddisfa tutti i requisiti di sicurezza (15+ car, 123, ABC, !)."""
    pwd = "PasswordSicura1!"
    assert is_strong_password(pwd) is True


def test_is_strong_password_false() -> None:
    """Testa una password che fallisce i criteri di sicurezza perché troppo corta."""
    pwd = "Abc12!"
    assert is_strong_password(pwd) is False


def test_generate_pin_is_numeric() -> None:
    """Verifica che il PIN generato contenga solo cifre e rispetti la lunghezza."""
    length = 6
    res = generate_pin(length)
    assert res.isdigit()
    assert len(res) == length


def test_cesar_cipher() -> None:
    """Verifica la correttezza della cifratura e della decifratura (inversione)."""
    original = "Abc1"
    shift = 3
    encrypted = cesar_cipher(original, shift)
    assert encrypted == "Def4"
    assert cesar_cipher(encrypted, -shift) == original
