class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_cycle(head):
  current = head
  seen = set()
  print(current)
  while current is not None:
    print(seen)
    if current in seen:
      return True
    seen.add(current)
    current = current.next
  return False

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d
d.next = b # cycle

#         _______
#       /        \
# a -> b -> c -> d 

linked_list_cycle(a)  # True


q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')
u = Node('u')

q.next = r
r.next = s
s.next = t
t.next = u
u.next = q # cycle

#    ________________
#  /                 \
# q -> r -> s -> t -> u 

linked_list_cycle(q)  # True
