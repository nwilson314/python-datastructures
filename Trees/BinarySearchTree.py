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

		self._count += 1

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

	def is_in_tree(self, val):
		'''Returns True if a value is in the tree. False otherwise'''

		return self._is_in_tree(self.root, val)

	def _is_in_tree(self, node, val):
		if node == None:
			return False
		elif node.val == val:
			return True
		elif val < node.val:
			return self._is_in_tree(node.left, val)
		else:
			return self._is_in_tree(node.right, val)

	def get_min(self):
		temp = self.root

		if temp == None:
			raise ValueError('The tree is empty!')

		while temp != None:
			temp2 = temp
			temp = temp.left

		return temp2.val


	def get_max(self):
		temp = self.root

		if temp == None:
			raise ValueError('The tree is empty!')

		while temp != None:
			temp2 = temp
			temp = temp.right

		return temp2.val


	def get_node_count(self):
		return self._count


	def print_tree(self):
		'''Prints values in tree from min to max'''
		if self.root == None:
			return ''
		else:
			s = []
			self._print(self.root, s)
			return ' '.join(s)

	def _print(self, node, s):
		'''Recursive helper for inorder printing'''
		if node == None:
			return 
		self._print(node.left, s)
		s.append(str(node.val))
		self._print(node.right, s)