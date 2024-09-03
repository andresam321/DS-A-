# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

                  #a      1
def zipper_lists(head_1, head_2): 
    tail = head_1  # Start with the head of the first list as the tail.
    count = 0  # Initialize a counter to keep track of iterations.
    current_one = head_1.next  # Set current_one to the next node of the first list.
    current_two = head_2  # Set current_two to the head of the second list.
    
    while current_one is not None and current_two is not None:
        if count % 2 == 0:  # On even iterations:
            tail.next = current_two  # Point the tail's next to the current node of the second list.
            current_two = current_two.next  # Move to the next node in the second list.
        else:  # On odd iterations:
            tail.next = current_one  # Point the tail's next to the current node of the first list.
            current_one = current_one.next  # Move to the next node in the first list.
        
        tail = tail.next  # Move the tail to the next node in the zipped list.
        count += 1  # Increment the counter.

    # After the loop, attach any remaining nodes from either list.
    if current_one is not None:
        tail.next = current_one
    if current_two is not None:
        tail.next = current_two
    
    return head_1  # Return the head of the zipped list.



"""
Explanation:
1. We start by assigning the `tail` variable to `head_1`, meaning the tail initially points to the first node of the first list. We also initialize a counter `count` to zero.
2. We create two pointers: `current_one` (pointing to the second node of the first list) and `current_two` (pointing to the head of the second list).
3. We enter a while loop that continues as long as there are nodes left in both lists (`current_one` and `current_two` are not None).
4. Inside the loop:
   - If the `count` is even, we attach the next node from the second list (`current_two`) to the zipped list and move `current_two` to the next node in the second list.
   - If the `count` is odd, we attach the next node from the first list (`current_one`) to the zipped list and move `current_one` to the next node in the first list.
   - We then move the `tail` pointer forward to continue building the zipped list and increment the counter.
5. Once the loop ends, we check if any nodes are left in either list. If so, we attach the remaining nodes to the end of the zipped list.
6. Finally, we return the head of the newly zipped list, which starts from `head_1`.


We start by defining a Node class to represent each node in a linked list, which includes a value and a reference to the next node in the list. We then create two separate linked lists: the first list (a -> b -> c) and the second list (x -> y -> z). To merge these lists in a “zippered” fashion, we invoke the zipper_lists function, passing in the heads of both lists (a and x).


Inside the function, we initialize a tail pointer, starting at the head of the first list (a), and set up two pointers, current_one and current_two, to traverse the remaining nodes of the first and second lists, respectively. We also initialize a counter to alternate between the two lists as we merge them.

In the first iteration, since the counter is even, we link the first node from the second list (x) to the tail and move the tail pointer to x. We then proceed to the next node in the second list (y). In the second iteration, since the counter is now odd, we link the next node from the first list (b) to the tail and move the tail pointer to b. We then move to the next node in the first list (c). This alternating process continues, linking nodes from each list until one list is exhausted.

In our case, after a few iterations, we successfully merge the lists into a -> x -> b -> y -> c. At this point, since there are no more nodes left in the first list, we append the remaining nodes from the second list, resulting in the final merged list: a -> x -> b -> y -> c -> z.
"""




### cases ###
# a = Node("a")
# b = Node("b")
# c = Node("c")
# a.next = b
# b.next = c
# # a -> b -> c

# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# # x -> y -> z

# zipper_lists(a, x)
# # a -> x -> b -> y -> c -> z


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# # a -> b -> c -> d -> e -> f

# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# # x -> y -> z

# zipper_lists(a, x)
# # a -> x -> b -> y -> c -> z -> d -> e -> f


# s = Node("s")
# t = Node("t")
# s.next = t
# # s -> t

# one = Node(1)
# two = Node(2)
# three = Node(3)
# four = Node(4)
# one.next = two
# two.next = three
# three.next = four
# # 1 -> 2 -> 3 -> 4

# zipper_lists(s, one)
# # s -> 1 -> t -> 2 -> 3 -> 4


# w = Node("w")
# # w

# one = Node(1)
# two = Node(2)
# three = Node(3)
# one.next = two
# two.next = three
# # 1 -> 2 -> 3 

# zipper_lists(w, one)
# # w -> 1 -> 2 -> 3
