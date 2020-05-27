class Node:
	'''
	Node class used in linked lists. Implented here as a doubly linked node.
	'''
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None