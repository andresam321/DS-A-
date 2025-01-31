# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque


def tree_levels(root):
  if root is None:
    return []
  levels = [] #[ ]
  queue = deque([ (root, 0) ])
  while queue:
    current, level_num = queue.popleft()  # 
#                                 levels level_num
    if len(levels) == level_num: ## 1 ,  1 
      levels.append([current.val])

    else:
      levels[level_num].append(current.val)
      
    if current.left is not None:
      queue.append((current.left, level_num + 1)) 

    if current.right is not None:
      queue.append((current.right, level_num + 1)) 
    
  return levels
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

#### recursion
def tree_levels(root):
  levels = []
  _tree_levels(root, levels, 0)
  return levels
  
def _tree_levels(root, levels, level_num):
  if root is None:
    return
  
  if level_num == len(levels):
    levels.append([ root.val ])
  else:
    levels[level_num].append(root.val)
  
  _tree_levels(root.left, levels, level_num + 1)
  _tree_levels(root.right, levels, level_num + 1)  
  


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

# tree_levels(a) # ->
# # [
# #   ['a'],
# #   ['b', 'c'],
# #   ['d', 'e', 'f']
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

# tree_levels(a) # ->
# # [
# #   ['a'],
# #   ['b', 'c'],
# #   ['d', 'e', 'f'],
# #   ['g', 'h', 'i']
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

# tree_levels(q) # ->
# # [
# #   ['q'],
# #   ['r', 's'],
# #   ['t'],
# #   ['u'],
# #   ['v']
# # ]



# tree_levels(None) # -> []
