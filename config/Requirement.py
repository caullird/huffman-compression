# Import of external libraries
from pathlib import Path
import os

# Importation of interfaces
from config.Interface.RequirementInterface import RequirementInterface

class Requirement(RequirementInterface):

	""" Class Requirement 

	@override : RequirementInterface

	Allows the management of the files necessary for the creation of the results

    """

	def __init__(self, folder_name: str):

		""" Constructor of the Requirement class

	    Parameters
	    ----------
		folder_name : str
			Path to the file

	    """

		self.folder_name = folder_name
		self.path = self.generate_path()


	""" Getters & Setters

    Function allowing the modification and recovery of the elements of the object

    Getters 
    ----------
    	- get_path(self) : is used to retrieve the "path" element 	

    """

	def get_path(self):
		return self.path


	def generate_path(self):

		"""Allows to generate the path and to check the good creation of the target file

		@override : generate_path(self) in RequirementInterface

	    Returns
	    -------
	    path : str

	    """

		if(not((os.path.isdir('data/' + self.folder_name)))):
			os.mkdir('data/' + self.folder_name)

		return 'data/' + str(self.folder_name) + '/'


