
class Frequence :
	def __init__(self,text,frequence = 0):
		self.text = text 
		self.frequence = self.calcul_frequence()

	def get_text(self):
		return self.text

	def get_frequence(self):
		return self.frequence

	def set_text(self, value):
		self.text = value

	def set_frequence(self, value):
		self.frequence = value

	def calcul_frequence(self):
		freq = {}

		for c in self.text:
		    if c in freq:
		        freq[c] += 1
		    else:
		        freq[c] = 1

		freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

		self.set_frequence(freq)

		return freq

		