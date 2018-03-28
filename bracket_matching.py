# Create a method called test_brackets that takes a string and determines if all brackets
# are correctly matching / nested (returns true or false). This is code could be used
# as part of a system to detect syntax errors in code.

# It should check for the following: [ ],{ },( )

class Stack:
  def __init__(self):
    self.store = list()

  def pop(self):
    self.store.pop()

  def push(self, element):
    self.store.append(element)

  def length(self):
    return len(self.store)

  def look(self):
    return self.store[-1]

def test_brackets(string):
  # using a simple list
  # stack = list()

  # using a Stack
  stack = Stack()

  char_map = {
    ')': '(',
    ']': '[',
    '}': '{'
  }

  for char in string:
    if char == '(' or char == '[' or char == '{':
      stack.push(char)
    elif char == ')' or char == ']' or char == '}':
      if stack.length() > 0 and char_map[char] == stack.look():
        stack.pop()
      else:
        return False

  if stack.length() > 0:
    return False
  else:
    return True

print(test_brackets('abc(123)'), 'should return true')
#returns true

print(test_brackets('abc(123'), 'should return false')
#returns false -- missing closing bracket

print(test_brackets('a[bc(123)]'), 'should return true')
#returns true

print(test_brackets('a[bc(12]3)'), 'should return false')
#returns false -- inproperly nested

print(test_brackets('a{b}{c(1[2]3)}'), 'should return true')
#returns true

print(test_brackets('a{b}{c(1}[2]3)'), 'should return false')
#returns false -- inproperly nested

print(test_brackets('()'), 'should return true')
#returns true

print(test_brackets('[]]'), 'should return false')
#returns false - no opening bracket to correspond with last character

print(test_brackets('abc123yay'), 'should return true')
#returns true -- no brackets = correctly matched
