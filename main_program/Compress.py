
# Import CompressInterface related to the current class
from main_program.Interface.CompressInterface import CompressInterface

class Compress(CompressInterface):

	""" Class Compress 

	@override : CompressInterface

	Used to compress a string given by the user

    """

	def compress_text(self, node:object, text:str):

		"""Used to compress a text in binary format

		@override : compress_text(self, node:object, text:str) in CompressInterface
		
	    Parameters
	    ----------
	    node : object
	    text : string 
	    	Text that needs to be analyzed

	    Returns
	    -------
	    result_bin : string
	        translation into binary
	    alphabet_compress : Dictionary 
			Dictionary of correspondence of each character

	    """

		alphabet_compress = self.get_alphabet_compress(node)

		result_bin = ""

		for letter in text:
			result_bin += alphabet_compress[letter]

		return result_bin, alphabet_compress


	def get_alphabet_compress(self, node:object):

		"""Allows you to determine the matching dictionary 

		@override : get_alphabet_compress(self, node:object) in CompressInterface
		
	    Parameters
	    ----------
	    node : object

	    Returns
	    -------
	    dictionnaire_binary : dictionary
	        Dictionary of correspondence of each character

	    """

		dictionary_binary = {}

		for leaf in node.get_leaf_list():
			string = ""

			for chemin in node.get_chemin_vers_node(leaf):
				if(chemin.get_value() != None):
					string += chemin.get_value()

			dictionary_binary[chemin.get_label()] = string

		return dictionary_binary