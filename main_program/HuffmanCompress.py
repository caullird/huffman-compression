from config.File import File

from main_program.Frequence import Frequence
from main_program.HuffmanTree import HuffmanTree
from main_program.Compress import Compress
from main_program.Ratio import Ratio

import requirements as require

class HuffmanCompress:

	def __init__(self,data):
		self.data = self.initilize_data(data)
		self.is_file = False
		self.compress = self.compress()

	def sef_is_file(self,data):
		self.is_file = data


	def initilize_data(self,data):

		file = File(require.initial_data + data)

		if(file.file_exist()):
			self.set_is_file(True)
			return file.open_file()
		
		return data


	def compress(self):

		# Gestion de la fréquence & écriture dans un fichier lex_ : 

		freq = Frequence(self.data)

		text_frequences = freq.get_frequence()

		file_freq = File(require.data_lexique_freq + "lex_" + self.data)

		file_freq.write_file_freq(text_frequences,self.is_file)

		# Gestion de la création de l'arbre

		tree = HuffmanTree()

		huffman_tree = tree.create_huffman_tree(text_frequences)

		# Gestion de la compression du texte

		compress = Compress()

		bin_textsimple,alphabet_binaire = compress.compress_text(huffman_tree,self.data)

		#TODO ///////////////////////////// fichier_compress = file_management.File(require.result_data + "result_" + config.FILE_NAME).write_file(bin_textsimple)

		#Gestion du ratio de compression

		ratio = Ratio(alphabet_binaire,text_frequences,self.data)

		ratio_percent = ratio.get_precent_save()

		print(ratio_percent)
