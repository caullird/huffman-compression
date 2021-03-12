# Import of external libraries
from os import path

# Importation of interfaces
from config.Interface.FileInterface import FileInterface

class File(FileInterface):

	""" Class File

	@override : FileInterface

	Global file management

    """

	def __init__(self, file):

		""" Constructor of the File class

	    Parameters
	    ----------
	    file : global file to be processed

	    """
		self.file = file 


	""" Getters & Setters

    Function allowing the modification and recovery of the elements of the object

    Getters 
    ----------
    	- get_file(self) : is used to retrieve the "file" element 	

    """

	def get_file(self):
		return self.file


	def open_file(self):

		"""Allows you to open a file

		@override : open_file(self) in FileInterface

	    Returns
	    -------
	    file 
	        Returns the content of the file
	    """

		return open(self.file, "r").read()


	def file_exist(self):

		"""Allows to check if the file exists or not

		@override : file_exist(self) in FileInterface

	    Returns
	    -------
	    boolean
	        True if it is a file, False if it is not a file
	    """

		if(path.exists(self.file)):
			return True
		
		return False 

	def write_file_freq(self,data: dict ,is_file: bool = False):


		"""Allows the writing of frequencies in a file

		@override : write_file_freq(self,data: dict ,is_file: bool) in FileInterface

		Parameters
	    ----------
	    data : dict
	        Dictionary of frequencies according to the characters
	    is_file : bool 
	    	Allows to know if it is a file or not

	    """

		if(is_file):
			f = open(self.file,"w")
		else: 
			f = open(self.file + ".txt","w")

		f.write(str(len(data)) + "\n")

		for value in data:
			f.write(str(value[0]) + " " + str(value[1]) + "\n")
		f.close()


	def write_file(self,data: str):


		"""Allows to write to the file in other cases (other than frequency)

		@override : write_file(self,data: str) in FileInterface

		Parameters
	    ----------
	    data : string
	        Character string given by the user

	    """

		f = open(self.file + ".txt","w+")

		f.write(data)




