'''
Main file to test arrays.
'''
from DynamicArray import DynamicArray

def test_dynamic_array():
	array = DynamicArray()
	print(len(array))

	array.append(1)
	print(len(array))
	print(array[0])

def main():
	test_dynamic_array()

if __name__ == "__main__":
	main()