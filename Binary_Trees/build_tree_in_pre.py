class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_pre(in_order, pre_order):
  if len(in_order) == 0:
    return None
  value = pre_order[0]
  root = Node(value)
  mid = in_order.index(value)
  left_in_order = in_order[:mid]
  right_in_order = in_order[mid + 1:]
  left_size = len(left_in_order)
  left_pre_order = pre_order[1: 1 + left_size]
  right_pre_order = pre_order[1 + left_size:]
  root.left = build_tree_in_pre(left_in_order, left_pre_order)
  root.right = build_tree_in_pre(right_in_order, right_pre_order)
  return root

build_tree_in_pre(
  [ 'z', 'y', 'x' ],
  [ 'y', 'z', 'x' ] 
)
#       y
#    /    \
#   z      x


build_tree_in_pre(
  [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
  [ 'a', 'b', 'd', 'e', 'g', 'h', 'c', 'f' ] 
)
#       a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h


build_tree_in_pre(
  [ 't', 'u', 's', 'q', 'r', 'p' ],
  [ 'u', 't', 's', 'r', 'q', 'p' ] 
)
#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p
