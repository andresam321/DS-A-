# from collections import deque 

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    
def lefty_nodes(root):
  values = []
  traverse(root, 0, values)
  return values

def traverse(root, level, values):
  if root is None:
    return

  if len(values) == level:
    values.append(root.val)

  traverse(root.left, level + 1, values)
  traverse(root.right, level + 1, values)

  # def lefty_nodes(root):
  
#   queue = deque([ (root, 0) ])
#   result = []
#   if root is None:
#     return [ ]
#   while queue:
#     current, level_num = queue.popleft()
#     if len(result) == level_num:
#       result.append(current.val)
    
#     if current.left is not None:
#       queue.append((current.left, level_num + 1 ))
#     if current.right is not None:
#       queue.append((current.right, level_num + 1))

#   print(result)
#   return result


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

lefty_nodes(a) # [ 'a', 'b', 'd', 'g' ]


u = Node('u')
t = Node('t')
s = Node('s')
r = Node('r')
q = Node('q')
p = Node('p')

u.left = t
u.right = s
s.right = r
r.left = q
r.right = p

#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p

lefty_nodes(u) # [ 'u', 't', 'r', 'q' ]


