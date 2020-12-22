import pytest

from BubbleSort import bubble_sort

class TestBubbleSort:
    def test1(self):
        arr = [1, 2, 3, 4, 5, 6, 7]

        assert bubble_sort(arr) == [1, 2, 3, 4, 5, 6, 7]

    def test2(self):
        arr = [1, 2, 3, 4, 5, 6, 7]

        arr.reverse()

        assert bubble_sort(arr) == [1, 2, 3, 4, 5, 6, 7]

    def test3(self):
        arr = [5, 4, 1, 6, 8, 10, 2, 4, 7]

        assert bubble_sort(arr) == [1, 2, 4, 4, 5, 6, 7, 8, 10]