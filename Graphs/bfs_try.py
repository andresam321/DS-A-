'''
travers through an adjancenly graph hitting all nodes from top to the bottom
make a queue variable that handles the start implementing deque 
then we make a list variable to push each node into that list
then we start iterating through the queue 
while queue 
node = queue.popleft()


for neighbor in graph[node]:
if the neighbor is in visited:
the we add the neighbor to visited so neighbors dont keep hitting each other indefintely 
return the result

'''

from collections import deque 

def bfs_try(graph, start):
    queue = deque([start])
    result = []
    visited = set([start])
    while queue:
        node = queue.popleft()

        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result
  
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(bfs_try(graph, 'f'))