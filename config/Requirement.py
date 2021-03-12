from pathlib import Path
import os

class Requirement:
	def __init__(self,folder_name):
		self.folder_name = folder_name
		self.path = self.generate_path()


	def generate_path(self):
		if(not((os.path.isdir('data/' + self.folder_name)))):
			os.mkdir('data/' + self.folder_name)

		return 'data/' + str(self.folder_name) + '/'


	def get_path(self):
		return self.path