def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)
  print(has_path(graph,node_A,node_B,set()))
  return has_path(graph, node_A, node_B, set())



def build_graph(edges):
  graph = {}


  
  for edge in edges:
    a, b = edge ## k and l
    
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
      
    graph[a].append(b)
    graph[b].append(a)
    
  return graph

def has_path(graph, src, dst, visited):
  if src == dst:
    return True
  
  if src in visited:
    return False
  
  visited.add(src)
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:
      return True
    
  return False
  


### test cases ####


# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

# undirected_path(edges, 'j', 'm') # -> True


# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

# undirected_path(edges, 'm', 'j') # -> True


# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

# undirected_path(edges, 'l', 'j') # -> True


# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

# undirected_path(edges, 'k', 'o') # -> False


# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

# undirected_path(edges, 'i', 'o') # -> False


# edges = [
#   ('b', 'a'),
#   ('c', 'a'),
#   ('b', 'c'),
#   ('q', 'r'),
#   ('q', 's'),
#   ('q', 'u'),
#   ('q', 't'),
# ]


# undirected_path(edges, 'a', 'b') # -> True


# edges = [
#   ('b', 'a'),
#   ('c', 'a'),
#   ('b', 'c'),
#   ('q', 'r'),
#   ('q', 's'),
#   ('q', 'u'),
#   ('q', 't'),
# ]

# undirected_path(edges, 'a', 'c') # -> True

# edges = [
#   ('b', 'a'),
#   ('c', 'a'),
#   ('b', 'c'),
#   ('q', 'r'),
#   ('q', 's'),
#   ('q', 'u'),
#   ('q', 't'),
# ]

# undirected_path(edges, 'r', 't') # -> True


# edges = [
#   ('b', 'a'),
#   ('c', 'a'),
#   ('b', 'c'),
#   ('q', 'r'),
#   ('q', 's'),
#   ('q', 'u'),
#   ('q', 't'),
# ]

# undirected_path(edges, 'r', 'b') # -> False


# edges = [
#   ('s', 'r'),
#   ('t', 'q'),
#   ('q', 'r'),
# ]

# undirected_path(edges, 'r', 't') # -> True
