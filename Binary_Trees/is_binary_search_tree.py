class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def is_binary_search_tree(root):
  values = []
  in_order_traversal(root, values)
  # print(values)
  return is_sorted(values)

def in_order_traversal(root, values):
  if root is None:
    return
  in_order_traversal(root.left, values)
  values.append(root.val)
  in_order_traversal(root.right, values)  

def is_sorted(numbers):
  for i in range(0, len(numbers) - 1):
    current = numbers[i]
    print("current",current)
    next = numbers[i + 1]
    print("next",next)
    #    5  <  3
    if next < current:
      return False
    
  return True

a = Node(12)
b = Node(5)
c = Node(15)
d = Node(3)
e = Node(9)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     15
#  / \     \
# 3   9     19

is_binary_search_tree(a) # -> True

# Time Complexity: O(n)
# You have to visit every node exactly once during the in-order traversal.

# No node is visited twice.

# Then, you iterate once through the list to check if it's sorted.

# So it's basically two O(n) operations:

# Traversal O(n)

# Checking if sorted O(n)

# Big-O ignores constants, so together, it's still O(n).

# Space Complexity: O(n)
# You are building a values list that stores every node’s value.

# So for n nodes, the list has n values → O(n) space.

# Also, recursion adds memory usage to the call stack.

# In the worst case (unbalanced tree, like a straight line), the recursion could go as deep as n.

# In a balanced tree, it's log(n) depth.

# But the list dominates because it's storing all n values explicitly.

# 👉 So overall space = O(n).