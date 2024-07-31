# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

# def tree_min_value(root):
#   list_of_val = []
#   queue = deque([root])
#   while queue:
#     current = queue.popleft()
#     list_of_val.append(current.val)

#     if current.right is not None:
#       queue.append(current.right)

#     if current.left is not None:
#       queue.append(current.left)
    
#   print(list_of_val)
#   return min(list_of_val)


# def tree_min_value(root): # 3,11,4,4,-2, 1
#   min_val = root.val
#   queue = deque([root]) #3 , 4 , 11 
#   while queue: #3 
#     current = queue.popleft() # 4
#     min_val = min(min_val,current.val) # 3, 3

#     if current.right is not None:
#       queue.append(current.right)

#     if current.left is not None:
#       queue.append(current.left)
    
#   return min_val

# def tree_min_value(root): # 3,11,4,4,-2, 1
#   smallest = float("inf")
#   stack = [root]
#   while stack: #3 
#     current = stack.pop() # 4
#     if current.val < smallest:
#       smallest = current.val

#     if current.right is not None:
#       stack.append(current.right)

#     if current.left is not None:
#       stack.append(current.left)
    
#   return smallest


def tree_min_value(root):
  if root is None: 
    return float('inf')

  left_min = tree_min_value(root.left)
  right_min = tree_min_value(root.right)

  return min(root.val,left_min, right_min)



### test cases ###

# a = Node(3)
# b = Node(11)
# c = Node(4)
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
# #   11     4
# #  / \      \
# # 4   -2     1
# tree_min_value(a) # -> -2


# a = Node(5)
# b = Node(11)
# c = Node(3)
# d = Node(4)
# e = Node(14)
# f = Node(12)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #       5
# #    /    \
# #   11     3
# #  / \      \
# # 4   14     12

# tree_min_value(a) # -> 3



# a = Node(-1)
# b = Node(-6)
# c = Node(-5)
# d = Node(-3)
# e = Node(-4)
# f = Node(-13)
# g = Node(-2)
# h = Node(-2)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #        -1
# #      /   \
# #    -6    -5
# #   /  \     \
# # -3   -4   -13
# #     /       \
# #    -2       -2

# tree_min_value(a) # -> -13
