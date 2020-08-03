import pytest
from BinarySearchTree import BST

def create_tree():
	b = BST()

	b.insert(5)
	b.insert(3)
	b.insert(4)
	b.insert(2)
	b.insert(3.5)
	b.insert(10)
	b.insert(8)
	b.insert(7)
	b.insert(11)

	return b

class TestBST:
	def test_node_count_empty(self):
		b = BST()

		assert b.get_node_count() == 0

	def test_print_tree(self):
		b = create_tree()
		out = b.print_tree()

		assert out == '2 3 3.5 4 5 7 8 10 11'

	def test_is_in_tree1(self):
		b = create_tree()

		assert b.is_in_tree(3.5) == True

	def test_is_in_tree2(self):
		b = create_tree()

		assert b.is_in_tree(12) == False

	def test_min(self):
		b = create_tree()

		assert b.get_min().val == 2

	def test_max(self):
		b = create_tree()

		assert b.get_max().val == 11

	def test_delete1(self):
		b = create_tree()

		b.delete_value(7)

		assert b.print_tree() == '2 3 3.5 4 5 8 10 11'

	def test_delete2(self):
		b = create_tree()

		b.delete_value(8)

		assert b.print_tree() == '2 3 3.5 4 5 7 10 11'

	def test_delete2(self):
		b = create_tree()

		b.delete_value(5)

		assert b.print_tree() == '2 3 3.5 4 7 8 10 11'