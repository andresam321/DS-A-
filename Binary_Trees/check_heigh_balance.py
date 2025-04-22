class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
def check_height_balance(root):
  if root is None:
    return 0

  left_height = check_height_balance(root.left)
  if left_height == -1:
    return -1

  right_height = check_height_balance(root.right)
  if right_height == -1:
    return -1

  if abs(left_height - right_height) > 1:
    return -1
  else:
    return 1 + max(left_height, right_height)

def is_tree_balanced(root):
  return check_height_balance(root) > -1

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.left = b
a.right = c
b.right = d

#         a
#       /   \
#      b    c
#      \
#      d

is_tree_balanced(a) # -> True
a = Node("a")
b = Node("b")
c = Node("c")

a.right = b
b.right = c

#        a
#         \
#          b
#          \
#           c

is_tree_balanced(a) # -> False
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

is_tree_balanced(a) # -> True
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
c.right = e
d.left = f

#        a
#      /   \
#     b     c
#    /      \
#   d        e
#  /
# f

is_tree_balanced(a) # -> False
