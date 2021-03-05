
class Ratio:

	def __init__(self,alphabet_binaire,text_frequences, uncompressed_file):

		self.alphabet_binaire = alphabet_binaire
		self.text_frequences = text_frequences
		self.uncompressed_file = uncompressed_file
		self.precent_save = self.calc_ratio()


	def get_uncompressed_file(self):
		return self.uncompressed_file

	def get_precent_save(self):
		return self.precent_save

	def get_alphabet_binaire(self):
		return self.alphabet_binaire

	def get_text_frequences(self):
		return self.text_frequences


	def calc_ratio(self):
		count_compress = 0
		count_initial = len(self.get_uncompressed_file())*8

		for letter_f in self.get_text_frequences():
			count_compress += int(len(self.get_alphabet_binaire()[letter_f[0]]) * letter_f[1])

		return float(count_compress/count_initial)

