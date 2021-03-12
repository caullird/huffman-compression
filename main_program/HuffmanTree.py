
# Importation of Huffman related classes
from main_program.Node import Node

# Import of external libraries
from operator import attrgetter

# Importation of interfaces
from main_program.Interface.HuffmanTreeInterface import HuffmanTreeInterface


class HuffmanTree(HuffmanTreeInterface):

	""" Class HuffmanTree 

	@override : HuffmanTreeInterface

	Allows to determine the tree for the compression

    """

	def create_node(self, data:dict, left_child:object = None, right_child:object = None):

		"""Allows to create a node in the tree

		@override : create_node(self, data:object ,left_child:object, right_child:object) in HuffmanTreeInterface

		Parameters
	    ----------
	    data : dict 
			- A letter with the frequency of occurrence

	    left_child : node => object
	    right_child : node => object

	    Returns
	    -------
	    object => Node
	        creation of a tree node
	    """

		if(right_child is None):

			if(left_child is None):

				# If the node has only one left child
				return Node(data[0], data[1])

			# If the node has only one right child
			return Node(data[0], data[1], left_child)

		# If the node has a left and a right child
		return Node(data[0], data[1], left_child, right_child)


	def create_huffman_tree(self, list_tupple:dict):

		"""Allows the construction of the tree

		@override : create_huffman_tree(self, list_tupple:dict) in HuffmanTreeInterface

		Parameters
	    ----------
	    list_tupple : dict 
			- The dictionary of letters with their frequency

	    Returns
	    -------
	    node : object
	    """

		list_node = []

		# Add all tupples as a node 
		for tupple in list_tupple:
			list_node.append(self.create_node(tupple))

		# We modify the set of nodes 
		while(len(list_node) > 1):
			list_node.sort(key=attrgetter('frequence'))

			# We take the two smallest and delete them
			n1 = list_node.pop(0)
			n2 = list_node.pop(0)

			# We create the new node 
			new_node = self.create_node(("NodeKey",n1.get_frequence() + n2.get_frequence()),n2,n1)
			list_node.append(new_node)	

			# We add the 1/0 correspondences for the future binary processing 
			self.add_node_value(list_node[0])

		return list_node[0]


	def add_node_value(self, node:object):

		"""Allows to assign a value to each node

		@override : add_node_value(self, node:object) in HuffmanTreeInterface

		Parameters
	    ----------
	    node : object 
			- The previously created node

	    Returns
	    -------
	    node : object
	    """

		left_child,right_child = node.get_left_child(),node.get_right_child()

		# If it is on the left, the value is 1
		if(left_child != None):
			left_child.set_value("1")
			self.add_node_value(left_child)

		# If it is on the right, the value is 0
		if(right_child != None):
			right_child.set_value("0")
			self.add_node_value(right_child)