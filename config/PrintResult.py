
class PrintResult:


	def __init__(self,text,text_frequences,bin_textsimple,alphabet_binaire,ratio_percent,nb_moyen):
		self.result = self.print_result(text,text_frequences,bin_textsimple,alphabet_binaire,ratio_percent,nb_moyen)

	def print_result(self,text,text_frequences,bin_textsimple,alphabet_binaire,ratio_percent,nb_moyen):
		
		print("\n"
			"##############################################"
			"\nResultat pour le texte suivant : \n" + 
			str(text) + 
			"\n##############################################"
			"\nAlphabet de fréquence :\n" + 
			str(text_frequences) + 
			"\n##############################################"
			"\nAlphabet binaire :\n" + 
			str(alphabet_binaire) + 
			"\n##############################################"
			"\nConversion du texte en binaire :\n" + 
			str(bin_textsimple) + 
			"\n##############################################"
			"\nRatio de compression :\n" + 
			str(ratio_percent) + 
			"\n##############################################"
			"\nNombre moyen de bits de stockage :\n" + 
			str(nb_moyen) + 
			"\n##############################################"
		)