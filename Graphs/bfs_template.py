##fifo, first in first out , queue

from collections import deque

def breadth_first(graph, start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        queue = queue.popleft()
        print(queue)
        while queue:
            for neighbor in graph[queue]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
