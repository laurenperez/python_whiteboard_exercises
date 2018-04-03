# uring recursion, write a binary search

a = [1, 3, 5, 7, 9, 11, 13, 15]

def binary_search(arr, num, start=0, end=None):
  if end is None:
    end = len(arr) - 1
  if start > end:
    return -1

  mid = (start + end) // 2

  if num < arr[mid]:
    return binary_search(arr, num, start, mid - 1)
  elif num > arr[mid]:
    return binary_search(arr, num, mid + 1, end)
  else:
    return mid


print(binary_search(a, 13))
