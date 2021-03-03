import sample.freq_management as freq_management
import sample.file_management as file_management
import sample.tree_management as tree_management
import sample.node_management as node_management
import requirements as require


class config():
	FILE_NAME = "bonjour.txt"


if __name__ == "__main__":

	text = file_management.File(require.data_need_to_be_convert + config.FILE_NAME).open_file().read()


	text_frequences = freq_management.Frequence(text).get_frequence()

	print(text_frequences)

	file_management.File(require.data_lexique_freq + "lex_" + config.FILE_NAME).write_file(text_frequences)


	huffman_tree = tree_management.HuffmanTree().create_huffman_tree(text_frequences)

	bin_textsimple = tree_management.HuffmanTree().compress_text(huffman_tree,text)





