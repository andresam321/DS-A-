# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# from collections import deque

# def tree_sum(root): #3 ,11, 4, 4, -2 ,1 
#   if not root:
#     return 0 
#   queue = deque([root]) # , , ,  , 1
#   total = 0
#   while queue:
#     node = queue.popleft() # 1
#     total += node.val # total = 3 + 11 + 4 + 4 - 2  + 1 = 21

#     if node.left:
#       queue.append(node.left) # 
#     if node.right:
#       queue.append(node.right)
#   print(total)
#   return total


# def tree_sum(root):
#   total = 0
#   if not root:
#     return 0

#   return root.val + tree_sum(root.left) + tree_sum(root.right)


# def depth_first_values(root):
#   if not root:
#     return []

#   left_values = depth_first_values(root.left)
#   right_values = depth_first_values(root.right)
#   return [root.val, *left_values, *right_values]


from collections import deque

def breadth_first_values(root):
  if not root:
    return []

  queue = deque([root])
  values = []

  while queue:
    node = queue.popleft()

    values.append(node.val)

    if node.left:
      queue.append(node.left)

    if node.right:
      queue.append(node.right)
  return values

###### TEST CASES #####

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

# tree_sum(a) # -> 21



# a = Node(1)
# b = Node(6)
# c = Node(0)
# d = Node(3)
# e = Node(-6)
# f = Node(2)
# g = Node(2)
# h = Node(2)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #      1
# #    /   \
# #   6     0
# #  / \     \
# # 3   -6    2
# #    /       \
# #   2         2

# tree_sum(a) # -> 10