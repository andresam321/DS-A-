# has_pathd takes in a dictionary 

## representing an adjancency kust of a directed acylic graph and two nodes

## it  

# def has_path(graph, src, dst):
#   if src == dst:
#     return True

#   for neighbor in graph[src]:
#     if has_path(graph, neighbor, dst) == True:
#       return True
#   return False


from collections import deque

def has_path(graph, src, dst):
  queue = deque([src])

  while queue:
    current = queue.popleft()
    if current == dst:
      return True

    for neighbor in graph[current]:
      queue.append(neighbor)
  return False


# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }

# has_path(graph, 'f', 'k') # True


# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }

# has_path(graph, 'f', 'j') # False
