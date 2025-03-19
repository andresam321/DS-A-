class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_palindrome(head):
  current = head
  result = []
  while current is not None:
    result.append(current.val)
    current = current.next
  print(result)
  return result == result[::-1]

a = Node(3)
b = Node(2)
c = Node(7)
d = Node(7)
e = Node(2)
f = Node(3)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 3 -> 2 -> 7 -> 7 -> 2 -> 3
linked_palindrome(a) # True

a = Node(3)
b = Node(2)
c = Node(4)

a.next = b
b.next = c

# 3 -> 2 -> 4
linked_palindrome(a) # False
