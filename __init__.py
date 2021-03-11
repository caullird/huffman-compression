from main_program.HuffmanCompress import HuffmanCompress
from tests.HuffmanTest import HuffmanTest


if __name__ == "__main__":


	# Chaine de caractère
	huffman = HuffmanCompress("bonjour!!")

	# Fichier
	#huffman = HuffmanCompress("bonjour.txt")
	

	#Fichiers de tests

	HuffmanTest().unitTest()
