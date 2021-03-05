
class Compress:

	#Fonction pour compression en différents formats, binaire....
	def compress_text(self,node,text):
		alphabet_compress = self.get_alphabet_compress(node)

		result_bin = ""

		for letter in text:
			result_bin += alphabet_compress[letter]

		return result_bin,alphabet_compress
		#return hex(int(result_bin,2))


	#Correspondance alphabet to binaire
	def get_alphabet_compress(self,node):
		list_chemin = {}

		for leaf in node.get_leaf_list():
			string = ""

			for chemin in node.get_chemin_vers_node(leaf):
				if(chemin.get_value() != None):
					string += chemin.get_value()

			list_chemin[chemin.get_label()] = string

		return list_chemin