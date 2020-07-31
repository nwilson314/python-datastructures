import pytest

from BinarySearch import binary_search, binary_search_recursion

class TestBinarySearch:
	def test1(self):
		arr = [1, 2, 3, 4, 5, 6, 7]

		val = 4

		assert binary_search(arr, val) == True

	def test2(self):
		arr = [1, 2, 3, 4, 5, 6, 7]

		val = 1

		assert binary_search(arr, val) == True


	def test3(self):
		arr = [1, 2, 3, 4, 5, 6, 7]

		val = 7

		assert binary_search(arr, val) == True

	def test4(self):
		arr = [1, 2, 3, 4, 5, 6, 7]

		val = 9

		assert binary_search(arr, val) == False


	def test5(self):
		arr = [1, 2, 3, 4, 5, 6, 7]

		val = 9

		assert binary_search_recursion(arr, val) == False

	def test6(self):
		arr = [1, 2, 3, 4, 5, 6, 7]

		val = 7

		assert binary_search_recursion(arr, val) == True

	def test7(self):
		arr = [1, 2, 3, 4, 5, 6, 7]

		val = 1

		assert binary_search_recursion(arr, val) == True	

