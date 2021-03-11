import unittest

from config.File import File

from main_program.Frequence import Frequence
from main_program.HuffmanTree import HuffmanTree
from main_program.Compress import Compress
from main_program.Ratio import Ratio

import requirements as require


class HuffmanTest(unittest.TestCase):
	def unitTest(self):
		print("\n\n")
		print("##############################################")
		print("Tests unitaires : ")
		unittest.main()

	def test_frequence(self):
		self.assertEqual(Frequence("bonjour!!").get_frequence(),[('o', 2), ('!', 2), ('b', 1), ('n', 1), ('j', 1), ('u', 1), ('r', 1)])


	def test_huffman_tree(self):
		freq = Frequence("bonjour!!")
		text_frequences = freq.get_frequence()

		tree = HuffmanTree()

		huffman_tree = tree.create_huffman_tree([('o', 2), ('!', 2), ('b', 1), ('n', 1), ('j', 1), ('u', 1), ('r', 1)])

		self.assertEqual(huffman_tree.get_left_child().get_right_child().get_right_child().get_label(),"j")
		self.assertEqual(huffman_tree.get_left_child().get_right_child().get_left_child().get_label(),"u")

	def test_compress(self):
		freq = Frequence("bonjour!!")
		text_frequences = freq.get_frequence()

		tree = HuffmanTree()
		huffman_tree = tree.create_huffman_tree(text_frequences)

		compress = Compress()
		bin_textsimple,alphabet_binaire = compress.compress_text(huffman_tree,"bonjour!!")

		self.assertEqual(bin_textsimple,"0101110111001111011100000")
		self.assertEqual(alphabet_binaire,{'!': '00', 'b': '010', 'n': '011', 'j': '100', 'u': '101', 'r': '110', 'o': '111'})


	def test_ratio(self):
		freq = Frequence("bonjour!!")
		text_frequences = freq.get_frequence()

		tree = HuffmanTree()
		huffman_tree = tree.create_huffman_tree(text_frequences)

		compress = Compress()
		bin_textsimple,alphabet_binaire = compress.compress_text(huffman_tree,"bonjour!!")

		ratio = Ratio(alphabet_binaire,text_frequences,"bonjour!!")

		ratio_percent = ratio.get_precent_save()
		nb_moyen = ratio.nombre_moyen()

		self.assertEqual(round(ratio_percent,3),0.347)
		self.assertEqual(round(nb_moyen,3),2.857)

	