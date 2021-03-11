from main_program.Node import Node

from operator import attrgetter


class HuffmanTree:

	def create_node(self, data,left_child = None, right_child = None):
		if(right_child is None):

			if(left_child is None):
				# None sans aucun enfant
				return Node(data[0],data[1])

			# Node avec uniquement la node de gauche 
			return Node(data[0],data[1],left_child)

		# Node avec gauche et droite
		return Node(data[0],data[1],left_child,right_child)

	def create_huffman_tree(self, list_tupple):
		list_node = []

		# Ajoute de tout les tupples en tant que noeud 
		for tupple in list_tupple:
			list_node.append(self.create_node(tupple))

		# On modifie l'ensemble des noeuds 
		while(len(list_node) > 1):
			list_node.sort(key=attrgetter('frequence'))

			# On prend les deux plus petits et on les supprimes
			n1 = list_node.pop(0)
			n2 = list_node.pop(0)

			# On crée le nouveau noeud 
			new_node = self.create_node(("NodeKey",n1.get_frequence() + n2.get_frequence()),n2,n1)
			list_node.append(new_node)	

			# On ajoute les correspondances 1/0 pour le futur traitement binaire 
			self.add_node_value(list_node[0])

		return list_node[0]


	def add_node_value(self, node):
		left_child,right_child = node.get_left_child(),node.get_right_child()

		# Si c'est à gauche, on met 1
		if(left_child != None):
			left_child.set_value("1")
			self.add_node_value(left_child)

		# Si c'est à droite, on met 0
		if(right_child != None):
			right_child.set_value("0")
			self.add_node_value(right_child)




		



