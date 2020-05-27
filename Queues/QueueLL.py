from LinkedListTail import LinkedListTail

class QueueLL:
	'''
	Implementation of a Queue using a linked list. Utilizes previously built
	Linked List with a tail pointer class.
	'''
	def __init__(self):
		self.ll = LinkedListTail()

	def enqueue(self, val):
		self.ll.push_back(val)

	def is_empty(self):
		return self.ll.is_empty()

	def dequeue(self):
		return self.ll.pop_front()