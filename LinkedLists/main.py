import pytest
from LinkedList import LinkedList
from LinkedListTail import LinkedListTail

class TestLinkedList:
	def test_is_empty(self):
		l = LinkedList()
		assert l.is_empty() == True

	def test_push_front(self):
		l = LinkedList()
		l.push_front(1)
		l.push_front(2)
		assert l.get_size() == 2

	def test_value_at_1(self):
		l = LinkedList()
		l.push_front(2)
		l.push_front(1)

		assert l.value_at(0) == 1

	def test_value_at_2(self):
		l = LinkedList()
		l.push_front(1)
		l.push_front(2)
		l.push_front(3)

		assert l.value_at(2) == 1

	def test_pop_front_1(self):
		l = LinkedList()

		l.push_front(1)
		l.push_front(2)

		assert l.pop_front() == 2

	def test_pop_front_2(self):
		l = LinkedList()

		l = LinkedList()

		l.push_front(1)
		l.push_front(2)
		l.pop_front()
		l.pop_front()

		assert l.is_empty() == True

	def test_push_back_1(self):
		l = LinkedList()

		l.push_back(1)
		l.push_back(2)

		assert l.value_at(1) == 2


	def test_pop_back_1(self):
		l = LinkedList()

		l.push_back(1)
		l.push_back(2)
		l.push_back(3)

		assert l.pop_back() == 3

	def test_back(self):
		l = LinkedList()
		l.push_back(1)
		l.push_back(2)
		l.push_back(3)

		assert l.back() == 3

	def test_insert1(self):
		l = LinkedList()

		l.push_back(1)
		l.push_back(2)
		l.push_back(3)

		i = 1

		l.insert(5, i)

		assert l.value_at(i) == 5

	def test_insert2(self):
		l = LinkedList()

		l.push_back(1)
		l.push_back(2)
		l.push_back(3)

		i = 1

		l.insert(5, i)

		assert l.value_at(i+1) == 2


	def test_print_list(self):
		l = LinkedList()
		l.push_front(1)
		l.push_front(2)
		l.push_front(3)

		i = 1

		l.insert(5, i)

		assert l.print_list() == '[3, 5, 2, 1]'

	def test_remove_at1(self):
		l = LinkedList()
		l.push_front(1)
		l.push_front(2)
		l.push_front(3)

		l.remove_at(1)

		assert l.print_list() == '[3, 1]'

class TestLinkedListTail:
	def test_init(self):
		l = LinkedListTail()
		assert l.get_size() == 0
