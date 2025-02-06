def longest_path(graph):
  distance = {}
## this checks for the last node that doesnt have any further connections 
## then it adds it
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0

  for node in graph:
      #                  graph  a     
    traverse_distance(graph, node , distance )
  return max(distance.values())


def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
    
  if len(graph[node]) == 0:  # If the node has no neighbors
      distance[node] = 0  # Terminal nodes have distance 0
      return 0 
    
  largest = 0
  for neighbor in graph[node]:
    attempt = traverse_distance(graph, neighbor, distance)
    if attempt > largest:
      largest = attempt
  
  distance[node] = 1 + largest
  return distance[node]


graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

longest_path(graph) # -> 2


graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

longest_path(graph) # -> 2


graph = {
  'h': ['i', 'j', 'k'],
  'g': ['h'],
  'i': [],
  'j': [],
  'k': [],
  'x': ['y'],
  'y': []
}

longest_path(graph) # -> 2

graph = {
  'a': ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'b': ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'c': ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'd': ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'e': ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'f': ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'g': ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'h': ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'i': ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'j': ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
  'k': ['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
  'l': ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
  'm': ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
  'n': ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
  'o': ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
  'p': ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
  'q': ['r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
  'r': ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
  's': ['t', 'u', 'v', 'w', 'x', 'y', 'z'],
  't': ['u', 'v', 'w', 'x', 'y', 'z'],
  'u': ['v', 'w', 'x', 'y', 'z'],
  'v': ['w', 'x', 'y', 'z'],
  'w': ['x', 'y', 'z'],
  'x': ['y', 'z'],
  'y': ['z'],
  'z': []
}

longest_path(graph) # -> 25
