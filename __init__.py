import sample.lex_management as lex_management
import sample.file_management as file_management
import sample.tree_management as tree_management
import requirements as require


class config():
	FILE_NAME = "bonjour.txt"


if __name__ == "__main__":

	text = file_management.File(require.data_need_to_be_convert + config.FILE_NAME).open_file().read()

	text_frequences = lex_management.Frequence(text).calcul_frequence()


	file_management.File(require.data_lexique_freq + "lex_" + config.FILE_NAME).write_file(text_frequences)

	print(text_frequences)






