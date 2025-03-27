from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
# def binary_search_tree_includes(root, target):
#   queue = deque([root])
#   results = []
#   while queue:
#     current = queue.popleft()
#     if current.val == target:
#       return True

#     if current.left is not None:
#       queue.append(current.left)
#     if current.right is not None:
#       queue.append(current.right)
#   return False
def binary_search_tree_includes(root, target):
  if root is None:
    return False
  
  if root.val == target:
    return True

  if target < root.val:
    return binary_search_tree_includes(root.left, target)
  else:
    return binary_search_tree_includes(root.right, target)
  

a = Node(12)
b = Node(5)
c = Node(18)
d = Node(3)
e = Node(9)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     18
#  / \     \
# 3   9     19


binary_search_tree_includes(a, 9) # -> True
binary_search_tree_includes(a, 12) # -> True