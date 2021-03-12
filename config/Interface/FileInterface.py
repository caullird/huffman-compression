
class FileInterface:

	def open_file(self):

		"""Allows you to open a file

		Use in File class

	    Returns
	    -------
	    file 
	        Returns the content of the file
	    """

		pass


	def file_exist(self):

		"""Allows to check if the file exists or not

		Use in File class

	    Returns
	    -------
	    boolean
	        True if it is a file, False if it is not a file
	    """

		pass 

	def write_file_freq(self,data: dict ,is_file: bool = False):


		"""Allows the writing of frequencies in a file

		Use in File class

		Parameters
	    ----------
	    data : dict
	        Dictionary of frequencies according to the characters
	    is_file : bool 
	    	Allows to know if it is a file or not

	    """

		pass


	def write_file(self,data: str):


		"""Allows to write to the file in other cases (other than frequency)

		Use in File class

		Parameters
	    ----------
	    data : string
	        Character string given by the user

	    """
		pass

