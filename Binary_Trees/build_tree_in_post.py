class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
#in_order : left, self, right
#post_order: left, right, self
def build_tree_in_post(in_order, post_order):
  if len(in_order) == 0:
    return None
  
  value = post_order[-1]
  root = Node(value)
  mid = in_order.index(value)
  left_in = in_order[:mid]
  right_in = in_order[mid + 1:]  
  left_post = post_order[:len(left_in)]
  right_post = post_order[len(left_in):-1]
  root.left = build_tree_in_post(left_in, left_post)
  root.right = build_tree_in_post(right_in, right_post)
  return root

# n = length of array
# Time: O(n^2)
# Space: O(n^2)
build_tree_in_post(
#in_order : left, self, right
  [ 'y', 'x', 'z' ],
#post_order: left, right, self  
  [ 'y', 'z', 'x' ] 
)
#       x
#    /    \
#   y      z
