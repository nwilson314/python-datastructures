import pytest

from HashTable import HashTable


class TestHashTable:
	def test_get_empty1(self):
		h = HashTable()

		assert h.get(5) == None

	def test_insert1(self):
		h = HashTable()
		h.insert(5, 10)

		assert h.get(5) == 10

	def test_resize1(self):
		m = 11
		h = HashTable(m=m)

		for i in range(m):
			h.insert(i, i+1)

		assert h.get_size() == m * 2 -1

	def test_resize2(self):
		m = 11
		h = HashTable(m=m)

		for i in range(m-2):
			h.insert(i, i+1)

		assert h.get(5) == 6

	def test_remove1(self):
		m = 11
		h = HashTable(m=m)

		for i in range(m):
			h.insert(i, i+1)

		h.remove(5)

		assert h.get(5) == None


