class HashMap():
  def __init__(self, size=128):
    self.size = size
    self.hashmap = [[None] for i in range(self.size)]

  def print_map(self):
    for item in self.hashmap:
      print(item)

  def put(self, key, value):
    hash_key = hash(key)
    hash_idx = hash_key % self.size
    if (self.hashmap[hash_idx][0] == None):
      self.hashmap[hash_idx][0] = {key: value}
    else:
      self.hashmap[hash_idx].append({key: value})

  def get(self, key):
    hash_key = hash(key)
    hash_idx = hash_key % self.size
    return self.hashmap[hash_idx]

  def remove(self, key):
    hash_key = hash(key)
    hash_idx = hash_key % self.size
    self.hashmap[hash_idx] = None



m = HashMap(10)
m.put('Lauren', "This is my string")
m.put('Steve', "This is steve's string")
m.put('Matt', "This is matt's string")
m.put('Jackson', "This is jackson's string")
m.print_map()


# this is after running it once - notice no collisions

# [{'Steve': "This is steve's string"}]
# [{'Jackson': "This is jackson's string"}]
# [None]
# [None]
# [None]
# [None]
# [None]
# [{'Matt': "This is matt's string"}]
# [{'Lauren': 'This is my string'}]
# [None]

# this is after running it again - notice 1 collision

# [None]
# [{'Matt': "This is matt's string"}]
# [{'Lauren': 'This is my string'}]
# [None]
# [None]
# [{'Steve': "This is steve's string"}, {'Jackson': "This is jackson's string"}]
# [None]
# [None]
# [None]
# [None]
