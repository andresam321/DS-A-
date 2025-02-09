class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


'''
print all nodes from the tree using either bfs or dfs 
##

if theres no root then just return an empty list
import deque from collections
then have queue = ([node])
then declare a result var = empty list to push each node into the list
first we are going to have to get the root node after we get the rood node we popleft to remove it from the queue then start
going for its neighbors but before we go to its neighbors we need to append the current val 
once we pop the node from the left we start iterating through the left and right side appending it to the queue 
checking its neighbors we need to have current.left / right then append the side its on
then we return our results 

'''
from collections import deque

def tree_try(root):
  if not root:
    return []
  queue = deque([root])
  result = []
  while queue:
    current = queue.popleft()

    result.append(current.val)
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
    
  return result

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_try(a)) # [3, 11, 4, 4, -2, 1]
