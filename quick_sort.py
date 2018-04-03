# array to sort
numbers = [9, 2, 5, 6, 4, 3, 7, 10, 1, 8]

def quickSort(array):

  less = []
  equal = []
  greater = []

  # stops spliting the array when it is down to 1 element
  if (len(array) < 2):
    return array

  if len(array) > 1:
    pivot = array[0]
    for i in array:
      if i < pivot:
        less.append(i)
      if i == pivot:
        equal.append(i)
      if i > pivot:
        greater.append(i)


  # this runs recursive quicksorts on the samller and smaller arrays while joining them back at the pivot
  return quickSort(less) + equal + quickSort(greater)


print(quickSort(numbers))
# [1,2,3,4,5,6,7,8,10]
