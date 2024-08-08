# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  paths = _all_tree_paths(root)
  for path in paths:
    path.reverse()
  return paths

def _all_tree_paths(root):
  if root is None:
    return []

  if root.left is None and root.right is None:
    return [[root.val]]

  all_paths = []

  left_sub_paths = _all_tree_paths(root.left)
  # [d,b,a ] 
  # [e,b,a]9
  for path in left_sub_paths:
    path.append(root.val) 
    all_paths.append(path)
    
  right_sub_paths = _all_tree_paths(root.right)
  for path in right_sub_paths:
    path.append(root.val)
    all_paths.append(path)

  return all_paths


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

# all_tree_paths(a) # ->
# # [ 
# #   [ 'a', 'b', 'd' ], 
# #   [ 'a', 'b', 'e' ], 
# #   [ 'a', 'c', 'f' ] 
# # ] 



# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# h = Node('h')
# i = Node('i')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# e.right = h
# f.left = i

# #         a
# #      /    \
# #     b      c
# #   /  \      \
# #  d    e      f
# #      / \    /   
# #     g  h   i 

# all_tree_paths(a) # ->
# # [ 
# #   [ 'a', 'b', 'd' ], 
# #   [ 'a', 'b', 'e', 'g' ], 
# #   [ 'a', 'b', 'e', 'h' ], 
# #   [ 'a', 'c', 'f', 'i' ] 
# # ] 



# q = Node('q')
# r = Node('r')
# s = Node('s')
# t = Node('t')
# u = Node('u')
# v = Node('v')

# q.left = r
# q.right = s
# r.right = t
# t.left = u
# u.right = v

# #      q
# #    /   \ 
# #   r     s
# #    \
# #     t
# #    /
# #   u
# #  /
# # v

# all_tree_paths(q) # ->
# # [ 
# #   [ 'q', 'r', 't', 'u', 'v' ], 
# #   [ 'q', 's' ] 
# # ] 


# z = Node('z')

# #      z

# all_tree_paths(z) # -> 
# # [
# #   ['z']
# # ]
