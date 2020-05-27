from LinkedList import LinkedList
from Node import Node

class LinkedListTail(LinkedList):
	'''
	Implementation of a Linked List with a tail pointer.
	'''

	def __init__(self):
		super().__init__()
		self.tail = None

	def push_front(self, val):
		'''
		Adds val to the front of the linked list.
		'''
		node = Node(val)
		node.next = self.head
		self.head = node
		if self.tail == None:
			self.tail = node
		self.size += 1


	def pop_front(self):
		'''
		Removes the first element of the linked list and returns its value.
		'''
		if self.is_empty():
			return IndexError('Pop from empty list')
		temp = self.head
		if self.tail == temp:
			self.tail = None

		self.head = self.head.next

		self.size -= 1

		return temp.val

	def push_back(self, val):
		'''
		Adds val to the back of the linked list.
		'''

		if self.head == None:
			self.head = Node(val)
			self.tail = self.head
		else:
			node = Node(val)
			self.tail.next = node
			self.tail = node

		self.size += 1


	def pop_back(self):
		'''
		Removes the last element of the linked list and returns its value.
		'''
		if self.is_empty():
			return IndexError('Pop from empty list')

		self.size -= 1
		temp1 = self.head
		if temp1.next == None:
			self.head = None
			return temp1.val

		temp2 = temp1.next

		while temp2.next != None:
			temp1 = temp2
			temp2 = temp2.next

		temp1.next = None
		self.tail = temp1
		return temp2.val