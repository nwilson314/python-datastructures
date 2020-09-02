import random

class HashTable:
	'''
	Implementation of a hash table using open addressing, linear probing with
	a universal hash function.

	Note that while this is as space efficient as possible (only using an array
	to store values), linear probing with a universal hash function has O(lgn)
	search, inserts, and deletes. A more efficient method costwise (but at the 
	cost of a space efficiency) is to use a double hashing method instead of 
	linear probing.
	'''

	_AVAIL = object()				# Deletion mark

	def __init__(self, m=11, p=109345121):
		self.min_m = 11				# Minimum size of table
		if m < self.min_m:
			self.m = self.min_m
		else:
			self.m = m				# Size of hash table
		self.n = 0					# Number of elements in the table
		self.T = [None] * self.m 	# The table
		self.p = p 					# Prime number used in hashing
		self.a = random.randint(1, p-1)
		self.b = random.randint(0, p-1)

	def get_size(self):
		'''
		Returns the capacity of the hash table.
		'''

		return self.m

	def insert(self, key, value):
		'''
		Inserts a key, value pair into the hash table. If the key already
		exists, the current value will be overwritten with the new one.
		'''
		if len(self.T) - 1 == self.n:
			self._resize(2 * self.m - 1)
		
		self._insert_into_table(key, value, self.T)
		self.n += 1

	def get(self, key):
		'''
		Gets and returns the value of the stored key in the table. If the key
		does not exist in the table, then None is returned.
		'''
		i = 0
		while i < len(self.T) - 1:
			j = self._hash(key, i)

			if self.T[j] == None:
				return None
			elif self.T[j] == HashTable._AVAIL:
				pass
			elif self.T[j][0] == key:
				return self.T[j][1]
			i += 1

		return None

	def exists(self, key):
		'''
		Checks if the key exists in the table. If it does, return True and False
		otherwise.
		'''
		if self.get(key) != None:
			return True
		return False

	def remove(self, key):
		'''
		Removes the key and its associated value from the table. In this
		implementation, a "deleted" flag is set at its location.
		'''
		i = 0
		while i < self.m:
			j = self._hash(key, i)
			if self.T[j] == None:
				break
			elif self.T[j] == HashTable._AVAIL:
				pass
			elif self.T[j][0] == key:
				self.T[j] = HashTable._AVAIL
				break
			i += 1

	def _resize(self, size):
		'''
		Resizes the given table based on the size passed. During the resizing
		any "delete" flags are removed and the keys are rehashed.
		'''
		new_T = [None] * size
		self.m = size
		self.a = random.randint(1, self.p-1)
		self.b = random.randint(0, self.p-1)

		for i in range(len(self.T)):
			if self.T[i] != None and self.T[i] != HashTable._AVAIL:
				self._insert_into_table(self.T[i][0], self.T[i][1], new_T)
		self.T = new_T

	def _insert_into_table(self, key, value, table):
		'''
		Inserts the key, value pair into the given table.
		'''

		i = 0
		while i < len(table) - 1:
			j = self._hash(key, i)
			if table[j] == None:
				table[j] = (key, value)
				break
			i += 1

	def _hash(self, key, i):
		'''
		Hashes the given key and iteration number. Returns the hashed value, 
		which is a position in the table to insert the key.

		The hash implemented is a universal hashing (Multiply, Add, Divide) with
		Linear probing.
		'''
		return (((self.a * hash(key) + self.b) % self.p) % self.m + i) % self.m




