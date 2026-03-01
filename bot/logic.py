import secrets 
import stirng

def generate_password(num_words: int=4) -> str:
	if num_words<4:
		raise ValueError("La lunghezza minima è 4 parole.")
	word_list=["aiuola","mela","nuvola","tastiera","fiume","scoglio","razzo","libro"]
	words=[]
	for _ in range(num_words):
		word=secrets.choice(word_list)
		words=secrets.append(word)
	return "-".join(words)	