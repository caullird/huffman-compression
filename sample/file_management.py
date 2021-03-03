
class File:

	def __init__(self,file):
		self.file = file 

	def get_file(self):
		return self.file

	def get_file(self, value):
		self.file = value

	def open_file(self):
		return open(self.file, "r")

	def write_file_freq(self,data):
		f = open(self.file,"w")

		f.write(str(len(data)) + "\n")

		for value in data:
			f.write(str(value[0]) + " " + str(value[1]) + "\n")
		f.close()

	def write_file(self,data):
		f = open(self.file,"w")

		f.write(data)





