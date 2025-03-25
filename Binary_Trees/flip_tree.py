class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def flip_tree(root):
  if root is None:
    return None
  left_path = flip_tree(root.left)
  right_path = flip_tree(root.right)
  root.left = right_path
  root.right = left_path

  return root

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

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

flip_tree(a) 

#       a
#    /    \
#   c      b
#  /     /   \
# f     e    d
#     /  \
#    h    g


u = Node("u")
t = Node("t")
s = Node("s")
r = Node("r")
q = Node("q")
p = Node("p")

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

flip_tree(u)

#           u
#        /    \
#       s      t
#      /
#     r
#    / \
#   p  q
