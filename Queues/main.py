import pytest

from QueueLL import QueueLL
from Queue import Queue

class TestQueueLL:
	def test_init(self):
		q = QueueLL()

	def test_is_empty(self):
		q = QueueLL()

		assert q.is_empty() == True

	def test_enqueue(self):
		q = QueueLL()

		q.enqueue(5)
		assert q.is_empty() == False

	def test_dequeue(self):
		q = QueueLL()

		q.enqueue(5)
		q.enqueue(6)
		q.enqueue(7)

		q.dequeue()

		assert q.dequeue() == 6


class TestQueue:
	def test_is_empty1(self):
		q = Queue(2)

		assert q.is_empty() == True


	def test_enqueue1(self):
		q = Queue(2)

		q.enqueue(1)

		assert q.is_empty() == False


	def test_enqueue_full(self):
		q = Queue(2)
		q.enqueue(1)

		with pytest.raises(IndexError):
			q.enqueue(2)

	def test_dequeue1(self):
		q = Queue(5)

		q.enqueue(1)
		q.enqueue(2)

		assert q.dequeue() == 1

	def test_dequeue_empty(self):
		q = Queue(2)

		with pytest.raises(IndexError):
			q.dequeue()
