# takes in a head of a linked list containing numbers as arguments  
#return total sum of all values in the linked list
class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None
#def sum_list(head)
# also need to add a sum variable and declare it at 0 and have it added before we move to the next node 
## iterate through the list once the he current head counted for we move the next node 
## return sum


def sum_list(head):
    current = head
    sum = 0
    while current is not None:
        sum += current.val
        current = current.next
    return sum

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19
