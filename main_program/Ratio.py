# Importation of interfaces
from main_program.Interface.RatioInterface import RatioInterface

class Ratio:

	""" Class Ratio

	@override : RatioInterface

	Allows you to calculate the compression ratio, and the character frequency rate

    """

	def __init__(self, alphabet_binaire:dict, text_frequences:dict, uncompressed_file:str):

		""" Constructor of the HuffmanCompress class

	    Parameters
	    ----------
	    alphabet_binaire : dic
	    	Correspondence of the characters  with their binanial value
	    text_frequences : dic
	    	Correspondence of the characters with their frequency
	    uncompressed_file : str
	    	Default string

	    """

		self.alphabet_binaire = alphabet_binaire
		self.text_frequences = text_frequences
		self.uncompressed_file = uncompressed_file
		self.precent_save = self.calc_ratio()

	""" Getters & Setters

    Function allowing the modification and recovery of the elements of the object

    Getters 
    ----------
    	- get_uncompressed_file(self) : is used to retrieve the "uncompressed_file" element 
    	- get_precent_save(self) : is used to retrieve the "percent_save" element 
    	- get_alphabet_binaire(self) : is used to retrieve the "alphabet_binaire" element 
    	- get_text_frequences(self) : is used to retrieve the "text_frequences" element     	

        
    """

	def get_uncompressed_file(self):
		return self.uncompressed_file

	def get_precent_save(self):
		return self.precent_save

	def get_alphabet_binaire(self):
		return self.alphabet_binaire

	def get_text_frequences(self):
		return self.text_frequences


	def calc_ratio(self):

		"""Allows you to determine the compression ratio

		@override : calc_ratio(self)

	    Returns
	    -------
	    ratio : float
	    	- Ratio corresponding to the compression rate on the initial rate

	    """

		count_compress = 0
		count_initial = len(self.get_uncompressed_file())*8

		for letter_f in self.get_text_frequences():
			count_compress += int(len(self.get_alphabet_binaire()[letter_f[0]]) * letter_f[1])

		return float(count_compress/count_initial)

	
	def character_avg(self):

		"""Allows to calculate the average weight of the characters

		@override : character_avg(self)

	    Returns
	    -------
	    avg : float
	    	average bits per character
	        
	    """

		somme = 0 

		arbre_binaire = self.get_alphabet_binaire()
		
		for letter in arbre_binaire.values():
			somme += len(letter)

		return(somme/len(arbre_binaire))


