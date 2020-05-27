

class Queue:
	'''
	Implementation of a queue using a fixed sized array (ring buffer).
	'''

	def __init__(self, size):
		self.a = [None] * size
		self.read = 0
		self.write = 0

	def is_empty(self):
		return self.read == self.write


	def enqueue(self, val):
		'''
		Adds the value to the back of the queue. The list provides a single 
		space buffer when adding in order to tell the difference between empty 
		and full queue
		'''
		if (self.write + 1) % len(self.a) == self.read:
			raise IndexError('The queue is full')

		self.a[self.write] = val
		self.write = (self.write + 1) % len(self.a)


	def dequeue(self):
		'''
		Removes and returns the least recently added value from the queue.
		'''
		if self.is_empty():
			raise IndexError('The queue is empty')

		val = self.a[self.read]

		self.read = (self.read + 1) % len(self.a)

		return val