
class Node:

	def __init__(self, label, frequence, left_child=None, right_child=None):
		self.label = label
		self.frequence = frequence
		self.left_child = left_child
		self.right_child = right_child
		self.value = None


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

	def set_value(self,value):
		self.value = value


	def is_leaf(self):
		return (self.get_right_child() is None) and (self.get_right_child() is None)

	def get_node_list(self):
		list_node = [self]
		if(not self.is_leaf()):
			if(not self.get_right_child() == None):
				list_node += self.get_right_child().get_node_list()
			list_node += self.get_left_child().get_node_list()
		return list_node

	def get_leaf_list(self):
		list_leaf = []
		list_node = self.get_node_list()
		for n in list_node:
			if(n.is_leaf()):
				list_leaf.append(n)
		return list_leaf

	def get_chemin_vers_node(self,default_node):
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



