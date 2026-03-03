import secrets 
import string

def generate_password(num_words: int=4) -> str:
	if num_words<4:
		raise ValueError("La lunghezza minima deve essere di 4 parole.")
	word_list=["aiuola","mela","nuvola","tastiera","fiume","scoglio","razzo","libro"]
	words=[]
	for _ in range(num_words):
		word=secrets.choice(word_list)
		words=secrets.append(word)
	return "-".join(words)	

def is_strong_password(password: str) -> bool:
	is_long_enough=len(password)>=15
	has_digit=False
	has_upper=False
	has_symbol=False
	for c in password:
		if c.isdigit():
			has_digit=True
		if c.isupper():
			has_upper=True
		if c in string.puntctuation:
			has_symbol=True
	return is_long_enough and has_digit and has_upper and has_symbol 	
