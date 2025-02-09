# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(node):
  if node is None:
    return -1
  stack = [(node, 0)]
  max_depth = -1
  while stack:
    current, depth = stack.pop()

    max_depth = max(max_depth,depth)
    if current.right is not None:
      stack.append((current.right, depth + 1))

    if current.left is not None:
      stack.append((current.left, depth + 1))

  return max_depth

# 0 0 0 0  0  0
# def how_high(node): 
#   if node is None:
#     return -1

#   left_height = how_high(node.left) # d
#   right_height = how_high(node.right) # e
#   return 1 + max(left_height, right_height)
#                     #-1         #-1        = 0
                    

### test cases ###

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

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

# how_high(a) # -> 2


# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# #    /
# #   g

# how_high(a) # -> 3



# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# #    /
# #   g

# how_high(a) # -> 3


# a = Node('a')
# c = Node('c')

# a.right = c

# #      a
# #       \
# #        c

# how_high(a) # -> 1


# a = Node('a')

# #      a

# how_high(a) # -> 0


# how_high(None) # -> -1
