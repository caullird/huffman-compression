import sample.freq_management as freq_management
import sample.file_management as file_management
import sample.tree_management as tree_management
import sample.node_management as node_management
import sample.ratio_management as ratio_management

import requirements as require


class config():
	FILE_NAME = "bonjour.txt"


if __name__ == "__main__":


	# Récupération de la chaine de caractère 
	
	file = file_management.File(require.initial_data + config.FILE_NAME)

	text = file.open_file()


	# Gestion de la fréquence & écriture dans un fichier lex_ : 

	freq = freq_management.Frequence(text)

	text_frequences = freq.get_frequence()

	file_freq =  file_management.File(require.data_lexique_freq + "lex_" + config.FILE_NAME)

	file_freq.write_file_freq(text_frequences)

	# Gestion de la création de l'arbre

	tree = tree_management.HuffmanTree()

	huffman_tree = tree.create_huffman_tree(text_frequences)

	# Gestion de la compression du texte

	bin_textsimple,alphabet_binaire = tree_management.HuffmanTree().compress_text(huffman_tree,text)

	#fichier_compress = file_management.File(require.result_data + "result_" + config.FILE_NAME).write_file(bin_textsimple)

	print(bin_textsimple)

	ratio = ratio_management.Ratio(alphabet_binaire,text_frequences,text).get_precent_save()


	print(ratio)


#TODO : 

'''

changmeent du nom des class
création arborescence 
creation d'un fichier config
creation class requirement config 
faciliter 

'''
