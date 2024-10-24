# largest_component({
#   0: [8, 1, 5],
#   1: [0],
#   5: [0, 8],
#   8: [0, 5],
#   2: [3, 4],
#   3: [2, 4],
#   4: [3, 2]
# }) # -> 4

def largest_component(graph): #
  visited = set()

  largest = 0

  for node in graph:
    size = explore_size(graph,node,visited)
    if size > largest:
      largest = size
      
  return largest


def explore_size(graph, node, visited):
  if node in visited:
    return 0
#0 8 5 1
  visited.add(node)

  size = 1
#1 #1 #1 #1 = 4
  for neighbor in graph[node]:
    size += explore_size(graph, neighbor, visited)

  return size


### test cases ###

largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4


largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 6


# largest_component({
#   3: [],
#   4: [6],
#   6: [4, 5, 7, 8],
#   8: [6],
#   7: [6],
#   5: [6],
#   1: [2],
#   2: [1]
# }) # -> 5


# largest_component({}) # -> 0


# largest_component({
#   0: [4,7],
#   1: [],
#   2: [],
#   3: [6],
#   4: [0],
#   6: [3],
#   7: [0],
#   8: []
# }) # -> 3
