import pytest
from BinarySearchTree import BST

class TestBST:
	def test_node_count_empty(self):
		b = BST()

		assert b.get_node_count() == 0