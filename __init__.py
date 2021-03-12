from main_program.HuffmanCompress import HuffmanCompress
from tests.HuffmanTest import HuffmanTest


if __name__ == "__main__":


	# Chaine de caractère
	#HuffmanCompress("bonjour!!", debug = True)

	# Fichier
	HuffmanCompress("alice.txt", debug = True)
	

	#Fichiers de tests

	HuffmanTest().unitTest()
