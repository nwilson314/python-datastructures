from Node import Node

class LinkedList:
	'''
	Implementation of a singly linked list.
	'''
	def __init__(self):
		self.head = None
		self.size = 0

	def get_size(self):
		'''
		Getter for the number of elements in the linked list
		'''
		return self.size

	def is_empty(self):
		'''
		Returns True if the linked list is empty, False otherwise.
		'''
		return self.size == 0