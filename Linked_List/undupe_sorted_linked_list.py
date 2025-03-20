class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def undupe_sorted_linked_list(head):
  current = head
  dummy_head = Node(None)
  tail = dummy_head
  while current is not None:
    if current.val != tail.val:
      tail.next = Node(current.val)
      tail = tail.next
    current = current.next
  return dummy_head.next
    
   
    

a = Node(4)
b = Node(4)
c = Node(6)
d = Node(6)
e = Node(6)
f = Node(7)
g = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

# 4 -> 4 -> 6 -> 6 -> 6 -> 7 -> 7

print(undupe_sorted_linked_list(a)) # 4 -> 6 -> 7