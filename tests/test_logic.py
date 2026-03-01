import pytest
from bot.logic import generate_password, is_strong_password, generate_pin, cesar_cipher

def test_generate_password_count():
	pwd=generate_password(10)
	assert len(pwd.split("-"))==10

def test_generate_password_min_length():
	with pytest.raises(ValueError):
		generate_password(3)

def test_is_strong_password_true():
	pwd="PasswordSicura1!"
	assert is_strong_password(pwd) is True

def test_is_strong_password_false():
	pwd="Abc12!"
	assert is_strong_password(pwd) is False
