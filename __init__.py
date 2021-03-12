from main_program.HuffmanCompress import HuffmanCompress
from tests.HuffmanTest import HuffmanTest


if __name__ == "__main__":


	# Chaine de caractère
	huffman = HuffmanCompress("bonjour!!", debug = True)

	# Fichier
	#huffman = HuffmanCompress("bonjour.txt", debug = False)
	

	#Fichiers de tests

	HuffmanTest().unitTest()
