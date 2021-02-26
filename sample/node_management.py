
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



