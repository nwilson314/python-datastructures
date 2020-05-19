'''
Main file to test arrays. Utilizes basic pytest commands
'''
from DynamicArray import DynamicArray
import pytest


class TestDynamicArrays:
	def test_append_indexing(self):
		arr = DynamicArray()
		arr.append(1)
		assert arr[0] == 1

	def test_append_len(self):
		arr = DynamicArray()
		arr.append(1)
		arr.append(2)
		assert len(arr) == 2

	def test_pop_no_i(self):
		a = DynamicArray()
		a.append(1)
		a.append(2)
		assert a.pop() == 2

	def test_pop_i(self):
		a = DynamicArray()
		a.append(2)
		a.append(1)
		a.append(4)
		assert a.pop(1) == 1

	def test_pop_len(self):
		a = DynamicArray()
		a.append(2)
		a.append(1)
		a.append(4)
		a.append(6)
		a.pop()
		assert len(a) == 3