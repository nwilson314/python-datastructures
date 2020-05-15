import ctypes

class DynamicArray:
	'''
	Custom version of the array already implemented in Python as a list. Uses
	ctypes to build the raw memory allocation.
	'''

	def __init__(self):
		self.size = 0
		self.capacity = 1
		self.array = self.create_array(self.capacity)


	def __len__(self):
		'''
		Returns number of elements in the array (size)
		'''
		return self.size

	def __getitem__(self, i):
		'''
		Gets and returns the item at the specified location in memory
		'''

		if i < 0 or i > self.size - 1:
			return IndexError('Index is out of bounds')

		return self.array[i]

	def append(self, val):
		'''
		Appends the value, val, to the end of the array
		'''

		if self.size == self.capacity:
			self._resize(self.capacity * 2)

		self.array[self.size] = val
		self.size += 1

	def create_array(self, cap):
		'''
		Returns a new array of the current capacity
		'''

		return (cap * ctypes.py_object)()

	def _resize(self, cap):
		'''
		Private function that resizes the array when it reaches
		capacity

		---> To implement
		'''

		return