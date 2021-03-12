
# Importing configuration classes
from config.File import File
from config.PrintResult import PrintResult
from config.Requirement import Requirement

# Importation of Huffman related classes
from main_program.Frequence import Frequence
from main_program.HuffmanTree import HuffmanTree
from main_program.Compress import Compress
from main_program.Ratio import Ratio

# Importation of interfaces
from main_program.Interface.HuffmanCompressInterface import HuffmanCompressInterface

class HuffmanCompress(HuffmanCompressInterface):


	""" Class HuffmanCompress 

	@override : HuffmanCompressInterface

	Core of the program, calling all functions

    """

	def __init__(self,data:str, debug:bool = False):

		""" Constructor of the HuffmanCompress class

	    Parameters
	    ----------
	    data : str
	    	String or file name
	    Debug : boolean
	        Allows to activate or not the debug mode (display of results)

	    """
		self.debug = debug
		self.paramater = data
		self.text = self.initilize_data(data)
		self.is_file = False
		self.compress = self.compress()


	""" Getters & Setters

    Function allowing the modification and recovery of the elements of the object

    Setters 
    ----------
    	- set_is_file(self,data:bool) : is used to modify the value of the "is_file" element
    	- set_data_name(self,data:str) : is used to modify the value of the "data_name" element
    	- set_paramater(self,data:str) : is used to modify the value of the "paramater" element
        
    """

	def set_is_file(self, data:bool):
		self.is_file = data

	def set_data_name(self, data:str):
		self.data_name = data

	def set_paramater(self, data:str):
		self.paramater = data


	def getDataName(self):

		"""Used to determine a name for the file

		Allows to distinguish between a string or a file

		@override : getDataName(self) in HuffmanCompressInterface

	    Returns
	    -------
	    string
	        File Name : Result of reading the file or the string
	    """

		if(self.is_file):
			return self.paramater
		else:
			return self.paramater[0:10]


	def initilize_data(self, data:str):

		"""Allows to read the file if it is a file

		Allows to distinguish between a string or a file

		@override : getDataName(self) in HuffmanCompressInterface

		Parameters
	    ----------
	    data : string
	        Character string given by the user

	    Returns
	    -------
	    data
	        Result of reading the file or the string
	    """

		file = File(Requirement("initial_data").get_path() + data)

		if(file.file_exist()):
			self.set_is_file(True)
			return file.open_file()

		return data


	def compress(self):

		"""Allows to call all the functions of the program to compress with the algorithm of huffman

		@override : compress(self) in HuffmanCompressInterface

	    """

	    # Creation of the aborescence of the results files

		frequence_data = Requirement("frequence_data")
		
		result_data = Requirement("result_data")

  		# Determine the frequency and write it to a file : 

		freq = Frequence(self.text)

		text_frequences = freq.get_frequence()

		file_freq = File(frequence_data.get_path() + "lex_" + self.text)

		file_freq.write_file_freq(text_frequences,self.is_file)

		# Creation of the tree corresponding to the string

		tree = HuffmanTree()

		huffman_tree = tree.create_huffman_tree(text_frequences)

		# Text compression with the tree

		compress = Compress()

		bin_textsimple,alphabet_binaire = compress.compress_text(huffman_tree,self.text)

		fichier_compress = File(result_data.get_path() + "result_" + self.text).write_file(bin_textsimple)

		# Determine compression ratios

		ratio = Ratio(alphabet_binaire,text_frequences,self.text)

		ratio_percent = ratio.get_precent_save()

		nb_avg = ratio.character_avg()


		if(self.debug):
			PrintResult(self.text,text_frequences,bin_textsimple,alphabet_binaire,ratio_percent,nb_avg)