import secrets 
import string 

def generate_password(num_words: int=4) -> str:
	if num_words<4:
		raise ValueError("la lunghezza minima è 4 parole")
		word_list=["aiuola", "mela", "nuvola", "tastiera", "fiume", "scoglio", "razzo", "libro"]
		words=[]
		for _ in range(num_words):
			word=secrets.choice(word_list)
			words.append(word)
		return "-".join(words)
