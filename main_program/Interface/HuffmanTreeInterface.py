
class HuffmanTreeInterface:

	""" Interface HuffmanTreeInterface 

	Use HuffmanTree

	Allows to determine the tree for the compression
 	"""

	def create_node(self, data:dict, left_child:object = None, right_child:object = None):

		"""Allows to create a node in the tree

		Use in HuffmanTree

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
		pass 

	def create_huffman_tree(self, list_tupple:dict):

		"""Allows the construction of the tree

		Use in HuffmanTree

		Parameters
		----------
		list_tupple : dict 
			- The dictionary of letters with their frequency

		Returns
		-------
		node : object
		"""
		pass


	def add_node_value(self, node:object):

		"""Allows to assign a value to each node

		Use in HuffmanTree

		Parameters
		----------
		node : object 
			- The previously created node

		Returns
		-------
		node : object
		"""

		pass
