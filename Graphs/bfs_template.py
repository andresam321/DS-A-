##fifo, first in first out , queue
'''
Using a list (default Python list):

Adding an element (append): O(1).
Removing an element (pop from the left): O(n).
In a standard list, removing an element from the front (pop(0)) 
requires shifting all the remaining elements one position to the left, 
which is an O(n) operation. This becomes inefficient as the number of nodes increases.
Using deque from the collections library:

Adding an element (append): O(1).
Removing an element (popleft): O(1).
deque (short for "double-ended queue") is optimized for both 
appending at the end and removing from the front in constant time (O(1)).


'''
from collections import deque

def breadth_first(graph, start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()  # Pop an element from the front of the queue
        print(node)
        
        for neighbor in graph[node]:  # Go through neighbors
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # Append unvisited neighbors


graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(breadth_first(graph, 'f'))