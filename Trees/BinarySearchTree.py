class Node:
	'''
	Node class used in BST.
	'''
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:
	'''Implementation of a binary search tree. Uses a mix of recursion and loops
	to practice both.
	'''

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
		if self.root == None:
			return None

		return self._get_min(self.root)

	def _get_min(self, node):
		if node.left == None:
			return node
		return self._get_min(node.left)

	def get_max(self):
		if self.root == None:
			return None
		return self._get_max(self.root)

	def _get_max(self, node):
		if node.right == None:
			return node
		return self._get_max(node.right)

	def delete_value(self, val):
		'''Deletes the specified value from the tree and returns its value'''
		self.root = self._delete(self.root, val)

	def _delete(self, node, val):
		'''Recursive deletion helper'''
		if node == None:
			# value not in tree
			return node
		if val < node.val:
			node.left = self._delete(node.left, val)
		elif val > node.val:
			node.right = self._delete(node.right, val)
		else:
			# Found node
			if not node.left:
				temp = node.right
				node = None
				return temp
			elif not node.right:
				temp = node.left
				node = None
				return temp
			else:
				# Two children
				temp = self._get_max(node.left)
				node.val = temp.val
				node.left = self._delete(node.left, temp.val)
		return node


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