from collections import deque


def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  visited = set([node_A])
  queue = deque([(node_A, 0)])

  while queue:
    node , distance = queue.popleft()

    if node == node_B:
      return distance

    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, distance + 1))
  return -1


def build_graph(edges):
  graph = {}

  for edge in edges:
    a, b = edge

    if not a in graph:
      graph[a] = []
    if not b in graph:
      graph[b] = [] 

    graph[a].append(b)
    graph[b].append(a)
  return graph



### test cases

# edges = [
#   ['w', 'x'],
#   ['x', 'y'],
#   ['z', 'y'],
#   ['z', 'v'],
#   ['w', 'v']
# ]

# shortest_path(edges, 'w', 'z') # -> 2


# edges = [
#   ['w', 'x'],
#   ['x', 'y'],
#   ['z', 'y'],
#   ['z', 'v'],
#   ['w', 'v']
# ]

# shortest_path(edges, 'y', 'x') # -> 1


# edges = [
#   ['a', 'c'],
#   ['a', 'b'],
#   ['c', 'b'],
#   ['c', 'd'],
#   ['b', 'd'],
#   ['e', 'd'],
#   ['g', 'f']
# ]

# shortest_path(edges, 'a', 'e') # -> 3


# edges = [
#   ['a', 'c'],
#   ['a', 'b'],
#   ['c', 'b'],
#   ['c', 'd'],
#   ['b', 'd'],
#   ['e', 'd'],
#   ['g', 'f']
# ]

# shortest_path(edges, 'e', 'c') # -> 2

# edges = [
#   ['a', 'c'],
#   ['a', 'b'],
#   ['c', 'b'],
#   ['c', 'd'],
#   ['b', 'd'],
#   ['e', 'd'],
#   ['g', 'f']
# ]

# shortest_path(edges, 'b', 'g') # -> -1


# edges = [
#   ['c', 'n'],
#   ['c', 'e'],
#   ['c', 's'],
#   ['c', 'w'],
#   ['w', 'e'],
# ]

# shortest_path(edges, 'w', 'e') # -> 1

# edges = [
#   ['c', 'n'],
#   ['c', 'e'],
#   ['c', 's'],
#   ['c', 'w'],
#   ['w', 'e'],
# ]

# shortest_path(edges, 'w', 'e') # -> 1

# edges = [
#   ['m', 'n'],
#   ['n', 'o'],
#   ['o', 'p'],
#   ['p', 'q'],
#   ['t', 'o'],
#   ['r', 'q'],
#   ['r', 's']
# ]

# shortest_path(edges, 'm', 's') # -> 6
