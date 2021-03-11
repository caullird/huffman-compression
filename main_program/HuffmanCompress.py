from config.File import File

from main_program.Frequence import Frequence
from main_program.HuffmanTree import HuffmanTree
from main_program.Compress import Compress
from main_program.Ratio import Ratio

import requirements as require

class HuffmanCompress:

	def __init__(self,data):
		self.paramater = data
		self.text = self.initilize_data(data)
		self.is_file = False
		self.compress = self.compress()

	def set_is_file(self,data):
		self.is_file = data

	def set_data_name(self,data):
		self.data_name = data

	def set_paramater(self,data):
		self.paramater = data

	def getDataName(self):
		if(self.is_file):
			return self.paramater
		else:
			return self.paramater[0:10]

	def initilize_data(self,data):

		file = File(require.initial_data + data)

		if(file.file_exist()):
			self.set_is_file(True)
			return file.open_file()
		return data


	def compress(self):

		# Gestion de la fréquence & écriture dans un fichier lex_ : 

		freq = Frequence(self.text)

		text_frequences = freq.get_frequence()


		file_freq = File(require.data_lexique_freq + "lex_" + self.text)

		file_freq.write_file_freq(text_frequences,self.is_file)

		# Gestion de la création de l'arbre

		tree = HuffmanTree()

		huffman_tree = tree.create_huffman_tree(text_frequences)

		# Gestion de la compression du texte

		compress = Compress()

		bin_textsimple,alphabet_binaire = compress.compress_text(huffman_tree,self.text)

		fichier_compress = File(require.result_data + "result_" + self.text).write_file(bin_textsimple)

		# Gestion du ratio de compression

		ratio = Ratio(alphabet_binaire,text_frequences,self.text)

		ratio_percent = ratio.get_precent_save()

		nb_moyen = ratio.nombre_moyen()

		self.write_result(text_frequences,bin_textsimple,alphabet_binaire,ratio_percent,nb_moyen)

	def write_result(self,text_frequences,bin_textsimple,alphabet_binaire,ratio_percent,nb_moyen):

		print("\n")
		print("##############################################")
		print("Resultat pour le texte suivant : ")
		print(self.text)
		print("##############################################")
		print("Alphabet de fréquence :")
		print(text_frequences)
		print("##############################################")
		print("Alphabet binaire :")
		print(alphabet_binaire)
		print("##############################################")
		print("Conversion du texte en binaire :")
		print(bin_textsimple)
		print("##############################################")
		print("Ratio de compression :")
		print(ratio_percent)
		print("##############################################")
		print("Nombre moyen de bits de stockage :")
		print(nb_moyen)
		print("##############################################")


