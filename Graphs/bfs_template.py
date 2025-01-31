##fifo, first in first out , queue

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