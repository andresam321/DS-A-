class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

##linked_list_find  that takes in the head of a link_list and a target value##
## if the current.val = target then return true ., false
def linked_list_find(head,target):
    current = head 
    while current is not None:
        if current.val == target:
            return True
        current = current.next 
    return False
    
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_find(a, "c")) # True
