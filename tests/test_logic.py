import pytest
from bot.logic import generate_password, is_strong_password, generate_pin, cesar_cipher

def test_generate_password_count():
	pwd=generate_password(10)
	assert len(pwd.split("-"))==10
