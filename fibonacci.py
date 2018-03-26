# Write a function that will print an array or list of fibonacci numbers to a specified length.
#
# Ex: fibonacci(10)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] - the first 10 numbers of the fibonacci sequence
#
# Hint:
# You may start your array like this:
# list = [0, 1]

// EX 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144


list = [0,1];

def fibonacci(count):
  start = 1
  list.append(start)
  next = start
  list.append(next)
  for i in range(2, count):
    list[i] = list[i-2] + list[i-1]

fibonacci(10)

print(list)
