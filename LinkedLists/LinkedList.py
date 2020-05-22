from Node import Node

class LinkedList:
	'''
	Implementation of a singly linked list without a tail pointer.
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

	def value_at(self, i):
		'''
		Gets the value at index i.
		'''

		if i < 0 or i >= self.size:
			return IndexError('Index is out of range.')

		index = 0
		temp = self.head

		while index < i:
			temp = temp.next
			index += 1

		return temp.val

	def push_front(self, val):
		'''
		Adds val to the front of the linked list.
		'''
		node = Node(val)
		node.next = self.head
		self.head = node
		self.size += 1

	def pop_front(self):
		'''
		Removes the first element of the linked list and returns its value.
		'''
		if self.is_empty():
			return IndexError('Pop from empty list')
		temp = self.head

		self.head = self.head.next

		self.size -= 1

		return temp.val

	def push_back(self, val):
		'''
		Adds val to the back of the linked list.
		'''

		if self.head == None:
			self.head = Node(val)
		else:
			temp = self.head
			while temp.next != None:
				temp = temp.next
			temp.next = Node(val)

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
		return temp2.val

	def front(self):
		'''
		Returns the value of the element at the front of the linked list.
		'''
		if self.is_empty():
			return None
		return self.head.val

	def back(self):
		'''
		Returns the value of the element at the back of the linked list.
		'''
		if self.is_empty():
			return None
		return self.value_at(self.size - 1)

	def insert(self, val, i):
		'''
		Inserts val at index i of the linked list
		'''
		if i < 0 or i > self.size:
			raise IndexError('Index out of range')

		if i == 0:
			self.push_front(val)
		elif i == self.size:
			self.push_back(val)
		else:
			index = 0
			temp = self.head

			while index < i - 1:
				temp = temp.next
				index += 1
			node = Node(val)
			node.next = temp.next
			temp.next = node

	def remove_at(self, i):
		'''
		Removes the value at position i
		'''

		if i < 0 or i >= self.size:
			raise IndexError('Index out of range')

		if i == 0:
			self.pop_front(val)
		elif i == self.size - 1:
			self.pop_back(val)
		else:
			index = 0
			temp = self.head

			while index < i - 1:
				temp = temp.next
				index += 1
			temp.next = temp.next.next

	def print_list(self):
		'''
		Prints the list the form of an array.
		'''

		s = '['
		temp = self.head
		while temp != None:
			if temp.next != None:
				s += str(temp.val) + ', '
			else:
				s += str(temp.val)
			temp = temp.next
		s += ']'

		return s


	def __str__(self):
		'''
		Overwrites the __str__ function in order to print the whole list
		'''

		return self.print_list()
		





















