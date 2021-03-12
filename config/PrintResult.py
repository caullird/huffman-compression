
class PrintResult:


	def __init__(self,text,text_frequences,bin_textsimple,alphabet_binaire,ratio_percent,nb_moyen):
		self.result = self.print_result(text,text_frequences,bin_textsimple,alphabet_binaire,ratio_percent,nb_moyen)

	def print_result(self,text,text_frequences,bin_textsimple,alphabet_binaire,ratio_percent,nb_moyen):
		print("\n")
		print("##############################################")
		print("Resultat pour le texte suivant : ")
		print(text)
		print("##############################################")
		print("Alphabet de fréquence :")
		print(text_frequences)
		print("##############################################")
		print("Alphabet binaire :")
		print(alphabet_binaire)
		print("##############################################")
		print("Conversion du texte en binaire :")
		print(bin_textsimple)
		print("##############################################")
		print("Ratio de compression :")
		print(ratio_percent)
		print("##############################################")
		print("Nombre moyen de bits de stockage :")
		print(nb_moyen)
		print("##############################################")