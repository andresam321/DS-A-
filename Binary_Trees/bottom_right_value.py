# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def bottom_right_value(root):
  queue = deque([root])
  while queue:
    current = queue.popleft()

    if current.left is not None:
      queue.append(current.left)
      
    if current.right is not None:
      queue.append(current.right)


  return current.val



### test cases ### 

# a = Node(3)
# b = Node(11)
# c = Node(10)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #       3
# #    /    \
# #   11     10
# #  / \      \
# # 4   -2     1

# bottom_right_value(a) # -> 1



# a = Node(-1)
# b = Node(-6)
# c = Node(-5)
# d = Node(-3)
# e = Node(-4)
# f = Node(-13)
# g = Node(-2)
# h = Node(6)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# e.right = h

# #        -1
# #      /   \
# #    -6    -5
# #   /  \     \
# # -3   -4   -13
# #     / \       
# #    -2  6

# bottom_right_value(a) # -> 6


# a = Node(-1)
# b = Node(-6)
# c = Node(-5)
# d = Node(-3)
# e = Node(-4)
# f = Node(-13)
# g = Node(-2)
# h = Node(6)
# i = Node(7)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# e.right = h
# f.left = i

# #        -1
# #      /   \
# #    -6    -5
# #   /  \     \
# # -3   -4   -13
# #     / \    /   
# #    -2  6  7 

# bottom_right_value(a) # -> 7




# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# a.left = b
# a.right = c
# b.right = d
# d.left = e
# e.right = f

# #      a
# #    /   \ 
# #   b     c
# #    \
# #     d
# #    /
# #   e
# #   \
# #    f
          
# bottom_right_value(a) # -> 'f'


# a = Node(42)

# #      42

# bottom_right_value(a) # -> 42
