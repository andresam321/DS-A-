class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def post_order(root):
  values = []
  post_traversal(root,values)
  return values
  
def post_traversal(root, values):
  if root is None:
    return
  post_traversal(root.left, values)
  post_traversal(root.right, values)
  values.append(root.val)

x = Node('x')
y = Node('y')
z = Node('z')

x.left = y
x.right = z

#       x
#    /    \
#   y      z

post_order(x)
# ['y', 'z', 'x']


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
  
#      a
#    /    \
#   b      c
#  / \    / \
# d   e  f   g

post_order(a)
# [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 


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

post_order(a)
# [ 'd', 'g', 'h', 'e', 'b', 'f', 'c', 'a' ] 
