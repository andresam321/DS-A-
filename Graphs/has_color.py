def can_color(graph):
  # declaring a dict 
  coloring = {}
  for node in graph:
    if node not in coloring:
      if not valid(graph, node, coloring, False):
        return False
  return False
  # todo

def valid(graph, node, coloring, current_color):
  if node in coloring:
    return current_color == coloring[node]

  coloring[node] = current_color
  for neighbor in graph[node]:
    if not valid(graph , neighbor, coloring, not current_color):
      return False
  return True
  
can_color({
  "x": ["y"],
  "y": ["x","z"],
  "z": ["y"]
}) # -> True
