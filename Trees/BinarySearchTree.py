class Node:
	'''
	Node class used in BST.
	'''
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:
	'''Implementation of a binary search tree'''

	def __init__(self):
		self.root = None
		self._count = 0

	def insert(self, val):
		if self.root == None:
			self.root = Node(val)
		else:
			self._insert(self.root, val)

		self.count += 1

	def _insert(self, root, val):
		'''Recusive helper for tree insertion'''
		if val < root.val:
			if root.left == None:
				root.left = Node(val)
			else:
				self._insert(root.left, val)
		else:
			if root.right == None:
				root.right = Node(val)
			else:
				self._insert(root.right, val)

	def get_node_count(self):
		return self._count


	def print_tree(self):
		'''Prints values in tree from min to max'''
		pass
