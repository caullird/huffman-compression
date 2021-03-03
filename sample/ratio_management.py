from pathlib import Path
import requirements as require

class Ratio:

	def __init__(self, uncompressed_file,compressed_file,file_name):
		self.uncompressed_file = uncompressed_file
		self.compressed_file = compressed_file
		self.file_name = file_name
		self.uncompressed_size = ""
		self.compressed_size = ""
		self.precent_save = self.calc_ratio()


	def get_uncompressed_file(self):
		return self.uncompressed_file

	def get_compressed_file(self):
		return self.compressed_file

	def get_file_name(self):
		return self.file_name

	def get_uncompressed_size(self):
		return self.uncompressed_size

	def get_compressed_size(self):
		return self.compressed_size

	def get_precent_save(self):
		return self.precent_save

	def set_uncomprossed_size(self,size):
		self.uncompressed_size = size

	def set_compressed_size(self,size):
		self.compressed_size = size

	def calc_ratio(self):

		self.set_uncomprossed_size(Path(require.initial_data + self.get_file_name()).stat().st_size)
		self.set_compressed_size(Path(require.result_data + "result_" + self.get_file_name()).stat().st_size)

		return 1 - (float(self.get_compressed_size())/float(self.get_uncompressed_size()))