def binary_search(arr, val):
	l = 0
	r = len(arr) - 1

	while l <= r:
		m = l + (r - l)//2
		if arr[m] == val:
			return True
		elif arr[m] < val:
			l = m + 1
		else:
			r = m - 1
	return False


def binary_search_recursion(arr, val):
	l = 0
	r = len(arr) - 1

	return bin_search_helper(arr, val, l, r)


def bin_search_helper(arr, val, l, r):
	m = l + (r - l)//2

	if arr[m] == val:
		return True
	elif l > r:
		return False
	elif arr[m] < val:
		l = m + 1
		return bin_search_helper(arr, val, l, r)
	else:
		r = m - 1
		return bin_search_helper(arr, val, l, r)
