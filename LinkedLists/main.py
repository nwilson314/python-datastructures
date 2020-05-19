import pytest
from LinkedList import LinkedList

class TestLinkedList:
	def test_is_empty(self):
		l = LinkedList()
		assert l.is_empty() == True