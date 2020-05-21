import ctypes

class DynamicArray:
	'''
	Ground up version of the array already implemented in Python as a list. Uses
	ctypes to build the raw memory allocation.

	Currently only implemented for 1-dim.
	'''

	def __init__(self):
		self.size = 0
		self.capacity = 1
		self.array = self._create_array(self.capacity)


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

	def pop(self, i=None):
		'''
		Returns the specified element at position i. If i is not specified, the 
		last element is returned. In addition, the specified element at location
		i is removed from the list.
		'''

		if i:
			if not self._checkIndexRange(i):
				return IndexError('Index is out of bounds')
			val = self.array[i]
			for j in range(i, self.size-1):
				self.array[j] = self.array[j+1]
				self.size -= 1
				return val
		else:
			self.size -= 1
			return self.array[self.size]

	def insert(self, val, i):
		'''
		Inserts a val at index i. Returns nothing.
		'''
		if not self._checkIndexRange(i):
			return IndexError('Index is out of bounds')

		if self.size == self.capacity:
			self._resize(self.capacity * 2)

		for j in range(self.size-1, i-1, -1):
			self.array[j+1] = self.array[j]

		self.array[i] = val
		self.size += 1


	def index(self, val):
		'''
		Returns the index of the first item in the list that matches val.
		Raises a ValueError if val is not in the array.
		'''

		for i in range(self.size):
			if self.array[i] == val:
				return i

		return ValueError('Value not found in the array')

	def _create_array(self, cap):
		'''
		Returns a new array of the current capacity
		'''

		return (cap * ctypes.py_object)()

	def _resize(self, cap):
		'''
		Private function that resizes the array when it reaches
		capacity

		'''

		new_array = self._create_array(cap)
		for i in range(self.size):
			new_array[i] = self.array[i]
		self.array = new_array

		self.capacity = cap

	def _checkIndexRange(self, i):
		'''
		Private function that checks if an index is out of bounds or not.
		Returns True if is within the valid range. False otherwise.
		'''

		return i >= 0 and i < self.size

