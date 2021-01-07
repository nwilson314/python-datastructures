'''
In place mergesort
'''

def merge_sort(l, r, arr):
    if l < r:
        m = l + (r - l) // 2

        merge_sort(l, m, arr)
        merge_sort(m+1, r, arr)

        merge(l, r, m, arr)

def merge(l, r, m, arr):
    i = l
    j = m + 1
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            i += 1
        else:
            temp_val = arr[j]
            temp_i = j

            while temp_i != i:
                arr[temp_i] = arr[temp_i - 1]
                temp_i -= 1

            arr[i] = temp_val
            i += 1
            m += 1
            j += 1

