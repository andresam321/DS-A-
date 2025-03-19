class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def middle_value(head):
  current = head
  result = []
  while current is not None:
    result.append(current.val)
    current = current.next 
  print(result)
  mid_idx = len(result) // 2
  print(mid_idx)
  mid_value = result[mid_idx]
  return mid_value

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.next = b
b.next = c
c.next = d
d.next = e

# a -> b -> c -> d -> e
middle_value(a) # c
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f
middle_value(a) # d

x = Node('x')
y = Node('y')
z = Node('z')

x.next = y
y.next = z

# x -> y -> z
middle_value(x) # y
