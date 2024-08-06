def tree_value_count(root, target):
 
  if root is None:
    return 0 

  count = 1 if root.val == target else 0

  return count + tree_value_count(root.left, target) + tree_value_count(root.right,target)




# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def tree_value_count(root, target):
#   if root is None:
#     return 0
#   count = 0
#   stack = [root]
#   while stack:
#     current = stack.pop()

#     if current.val == target:
#       count += 1


#     if current.right is not None:
#       stack.append(current.right)

#     if current.left is not None:
#       stack.append(current.left)

#   return count



### test cases ###


# a = Node(12)
# b = Node(6)
# c = Node(6)
# d = Node(4)
# e = Node(6)
# f = Node(12)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      12
# #    /   \
# #   6     6
# #  / \     \
# # 4   6     12

# tree_value_count(a,  6) # -> 3


# a = Node(12)
# b = Node(6)
# c = Node(6)
# d = Node(4)
# e = Node(6)
# f = Node(12)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      12
# #    /   \
# #   6     6
# #  / \     \
# # 4  6     12

# tree_value_count(a,  12) # -> 2

# a = Node(7)
# b = Node(5)
# c = Node(1)
# d = Node(1)
# e = Node(8)
# f = Node(7)
# g = Node(1)
# h = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #      7
# #    /   \
# #   5     1
# #  / \     \
# # 1   8     7
# #    /       \
# #   1         1

# tree_value_count(a, 1) # -> 4


# a = Node(7)
# b = Node(5)
# c = Node(1)
# d = Node(1)
# e = Node(8)
# f = Node(7)
# g = Node(1)
# h = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #      7
# #    /   \
# #   5     1
# #  / \     \
# # 1   8     7
# #    /       \
# #   1         1

# tree_value_count(a, 9) # -> 0
