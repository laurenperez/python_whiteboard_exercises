#Implement a program that prints out a half-pyramid of a specified height.


# makes a pyramid going up
def mario():
  num = input("How many levels should it be?")
  num = int(num)
  if num < 0 or num > 23:
    return mario()
  else:
    hashs = 1
    spaces = num
    while hashs <= num:
      print(" " * spaces + "#" * hashs)
      hashs += 1
      spaces -= 1

mario()


# makes a pyramid going down
def mario():
  num = input("How many levels should it be? ")
  num = int(num)
  if num < 0 or num > 23:
    return mario()
  else:
    count = 0
    draw = "#"
    while count < num:
      print(draw)
      draw+= "#"
      count+= 1

mario()


# makes a whole pyramid
def mario():
  num = input("How many levels should it be?")
  num = int(num)
  if num < 0 or num > 23:
    return mario()
  else:
    spaces = num-1
    hashes = 1
    while hashes <= num:
      print(" " * spaces + "#" * hashes + "  " + "#" * hashes + " " * spaces)
      spaces -= 1
      hashes += 1


mario()
