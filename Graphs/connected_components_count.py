def connected_components_count(graph):
  visited = set()
  count = 0

  for node in graph:
    if explore(graph, node,visited) == True:
      count += 1
  return count



def explore(graph, current, visited): #0: [8,1,5]
  if current in visited:
    return False

  visited.add(current)

  for neighbor in graph[current]:
    explore(graph, neighbor,visited)

  return True 


### test cases ###

# connected_components_count({
#   0: [8, 1, 5],
#   1: [0],
#   5: [0, 8],
#   8: [0, 5],
#   2: [3, 4],
#   3: [2, 4],
#   4: [3, 2]
# }) # -> 2


# connected_components_count({
#   1: [2],
#   2: [1,8],
#   6: [7],
#   9: [8],
#   7: [6, 8],
#   8: [9, 7, 2]
# }) # -> 1


# connected_components_count({
#   3: [],
#   4: [6],
#   6: [4, 5, 7, 8],
#   8: [6],
#   7: [6],
#   5: [6],
#   1: [2],
#   2: [1]
# }) # -> 3


# connected_components_count({}) # -> 0


# connected_components_count({
#   0: [4,7],
#   1: [],
#   2: [],
#   3: [6],
#   4: [0],
#   6: [3],
#   7: [0],
#   8: []
# }) # -> 5
