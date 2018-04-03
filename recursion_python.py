def recursion(n):
  if n == 0:
    print('Done')
  else:
    print(n)
    recurse(n-1)

recurse(10)

# Output
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Done


def plus(n):
  if n < 0:
    return 0
  else:
    return n + plus(n-1)


print(plus(10))

# Output
# 55


# empty string is a palendrome
# 1 char is a palendrome

def is_palindrome(s):
  # remove white spaces from the string
  s = s.replace(' ', '')
  # then check for our base cases
  if len(s) == 0 or len(s) == 1:
    return True
  elif s[0] != s[-1]:
    return False
  return is_palindrome(s[1:-1])

print(is_palindrome('tacocat'))
print(is_palindrome('a man a plan a canal panama'))
