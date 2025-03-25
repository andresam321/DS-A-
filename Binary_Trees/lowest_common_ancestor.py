class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def lowest_common_ancestor(root, val1, val2):
  path_1 = get_path(root, val1)
  print("path_1",path_1)
  path_2 = get_path(root, val2)
  print("path_2",path_2)
  set2 = set(path_2)
  print("set",set2)
  for val in path_1:
    if val in set2:
      return val
    
def get_path(root, target_val):
  if root is None:
    return None
  if root.val == target_val:
    return [ root.val ]

  left_path = get_path(root.left, target_val)
  if left_path is not None:
    left_path.append(root.val)
    return left_path
  right_path = get_path(root.right, target_val)
  if right_path is not None:
    right_path.append(root.val)
    return right_path
 
  return None
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
lowest_common_ancestor(a, 'd', 'h') # b
lowest_common_ancestor(a, 'd', 'h') # b
l = Node('l')
m = Node('m')
n = Node('n')
o = Node('o')
p = Node('p')
q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')

l.left = m
l.right = n
n.left = o
n.right = p
o.left = q
o.right = r
p.left = s
p.right = t

#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t
lowest_common_ancestor(l, 'q', 'r') # o
lowest_common_ancestor(l, 's', 't') # p