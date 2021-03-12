
# Import FrequenceInterface related to the current class
from main_program.Interface.FrequenceInterface import FrequenceInterface

class Frequence(FrequenceInterface) :

	""" Class Frequence 

	@override : FrequenceInterface

	Used to initialise a frequency object to determine a frequency table

    """


	def __init__(self, text:str, frequence:int = 0):

		""" Constructor of the Frequence class

	    Parameters
	    ----------
	    text : str
	    	Text in string form given by the user
	    frequence : int
	        variable that contains the frequency related to the parameter given by the user

	    """

		self.text = text 
		self.frequence = self.calcul_frequence(text)


	""" Getters & Setters

    Function allowing the modification and recovery of the elements of the object

    Getters
    ----------
    	- get_text(self) : is used to retrieve the "text" element
    	- get_frequence(self) : is used to retrieve the "frequence" element 

    Setters 
    ----------
    	- set_frequence(self,value) : is used to modify the value of the "frequence" element
    	- set_text(self,value) : is used to modify the value of the "text" element
        
    """

	def get_text(self):
		return self.text

	def get_frequence(self):
		return self.frequence

	def set_text(self, value:str):
		self.text = value

	def set_frequence(self, value:dict):
		self.frequence = value

	def calcul_frequence(self, text:str):

		"""Used to determine the frequency from a given string of characters

		@override : calcul_frequence(self,text:str) in FrequenceInterface

	    Parameters
	    ----------
	    text : string
	        Character string given by the user

	    Returns
	    -------
	    Dictionary
	        Dictionary with the corresponding letter frequency 
	    """

		freq = {}

		for c in text:
		    if c in freq:
		        freq[c] += 1
		    else:
		        freq[c] = 1

		freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)

		self.set_frequence(freq)

		return freq

		