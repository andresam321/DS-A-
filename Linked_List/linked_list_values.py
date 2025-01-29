
class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None


##takes a head of a linked list as an arument # should return all list values

def linked_list_values(head):
    allList = []
    current = head
    while current is not None:
        allList.append(current.val)
        current = current.next
    return allList
    



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_values(a)) # -> [ 'a', 'b', 'c', 'd' ]
