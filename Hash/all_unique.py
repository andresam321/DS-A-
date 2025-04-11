# def all_unique(items):
#   obj_items = {}
#   for ele in items:
#     # print(ele)
#     if ele not in obj_items:
#       obj_items[ele] = 0
#     obj_items[ele] += 1
#   # print(obj_items)
#   for key, value, in obj_items.items():
#     # print(key,value)
#     if value != 1:
#       return False
#   return True

def all_unique(items):
  set_items = set(items)
  print(set_items)
  if len(items) == len(set_items):
    return True
  return False

all_unique(["q", "r", "s", "a", "r", "z"]) # -> False
all_unique(["red", "blue", "yellow", "green", "orange"]) # -> True
all_unique(["cat", "cat", "dog"]) # -> False
all_unique(["a", "u", "t", "u", "m", "n"]) # -> False
