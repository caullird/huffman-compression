import sample.lex_management as lex_management
import sample.file_management as file_management
import sample.tree_management as tree_management
import requirements as require


if __name__ == "__main__":

	text = file_management.File(require.data_need_to_be_convert + "bonjour.txt").open().read()

	lex_text = lex_management.Frequence(text).calcul_frequence()

	print(lex_text)






