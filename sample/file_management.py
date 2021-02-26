class File:

	def __init__(self,file):
		self.file = file 

	def get_file(self):
		return self.file

	def get_file(self, value):
		self.file = value

	def open(self):
		return open(self.file, "r")


