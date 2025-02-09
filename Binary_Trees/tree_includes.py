# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# from collections import deque

# breadth first search

# def tree_includes(root, target): # a,b,c,d,e,f,
#   if root is None:
#     return False

#   queue = deque([root])

#   while queue:
#     current = queue.popleft()

#     if current.val == target: #              target = e
#       return True 
  
#     if current.left is not None:
#       queue.append(current.left)
#     if current.right is not None:
#       queue.append(current.right)
  
#   return False


#depth first search
def tree_includes(root, target): # a,b,c,d,e,f,
  if root is None:
    return False

  stack = [root]

  while stack:
    current = stack.pop()

    if current.val == target: #              target = e
      return True 
  
    if current.left is not None:
      stack.append(current.left)
    if current.right is not None:
      stack.append(current.right)
  
  return False


### test cases ###

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# tree_includes(a, "e") # -> True


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# tree_includes(a, "a") # -> True


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# tree_includes(a, "n") # -> False


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# #    /       \
# #   g         h

# tree_includes(a, "f") # -> True
