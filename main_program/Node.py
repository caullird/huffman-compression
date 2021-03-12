
# Importation of interfaces
from main_program.Interface.NodeInterface import NodeInterface

class Node(NodeInterface):

	def __init__(self, label:str, frequence:int, left_child:object = None, right_child:object = None):

		""" Constructor of the Frequence class

	    Parameters
	    ----------
	    label : str
	    	Text in string form given by the user
	    frequence : int
	        variable that contains the frequency related to the parameter given by the user
	    left_child : object => Node
	    right_child : object => Node

	    """

		self.label = label
		self.frequence = frequence
		self.left_child = left_child
		self.right_child = right_child
		self.value = None


	""" Getters & Setters

    Function allowing the modification and recovery of the elements of the object

    Getters
    ----------
    	- get_left_child(self) : is used to retrieve the "left_child" element
    	- get_right_child(self) : is used to retrieve the "right_child" element 
    	- get_label(self) : is used to retrieve the "label" element 
    	- get_frequence(self) : is used to retrieve the "frequence" element 
    	- get_value(self) : is used to retrieve the "value" element 


    Setters 
    ----------
    	- set_value(self,value:str) : is used to modify the value of the "value" element
        
    """

	def get_left_child(self):
		return self.left_child

	def get_right_child(self):
		return self.right_child

	def get_label(self):
		return self.label

	def get_frequence(self):
		return self.frequence

	def get_value(self):
		return self.value

	def set_value(self,value:str):
		self.value = value


	def is_leaf(self):

		"""Allows to know if it is a leaf or not

		@override : is_leaf(self) in NodeInterface

	    Returns
	    -------
	    boolean
	    	Returns true if it is a leaf, or false otherwise
	    """

		return (self.get_right_child() is None) and (self.get_right_child() is None)

	def get_node_list(self):

		"""Allows you to determine the list of nodes

		@override : get_node_list(self) in HuffmanCompressInterface

	    Returns
	    -------
	    liste_node
	    	- allows you to retrieve the list of nodes
	        
	    """

		list_node = [self]

		if(not self.is_leaf()):

			if(not self.get_right_child() == None):
				list_node += self.get_right_child().get_node_list()
			list_node += self.get_left_child().get_node_list()

		return list_node

	def get_leaf_list(self):

		"""Allows you to determine the list of leaf

		@override : get_leaf_list(self) in HuffmanCompressInterface

	    Returns
	    -------
	    list_leaf
	    	- allows you to retrieve the list of leaf
	        
	    """

		list_leaf = []
		list_node = self.get_node_list()

		for n in list_node:
			if(n.is_leaf()):
				list_leaf.append(n)

		return list_leaf

	def get_chemin_vers_node(self,default_node:object):

		"""allows to determine the path to the node

		@override : get_chemin_vers_node(self,default_node:object)

		Parameters
	    ----------
	    default_node : object

	    Returns
	    -------
	    list_leaf
	    	- allows you to retrieve the list of leaf
	        
	    """

		path = []
		list_node = self.get_node_list()

		while self != default_node:
			for node in list_node:
				if(node.get_left_child() == default_node or node.get_right_child() == default_node):
					path.append(default_node)
					default_node = node

		path.append(self)
		path.reverse()

		return path



