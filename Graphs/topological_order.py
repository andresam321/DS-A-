def topological_order(graph):
  num_parents = {}
  for node in graph:
    num_parents[node] = 0
    
  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1
  
  ready = [ node for node in graph if num_parents[node] == 0 ]
  order = []
  while ready:
    node = ready.pop()
    order.append(node)
    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)
    
  return order




topological_order({
  "a": ["f"],
  "b": ["d"],
  "c": ["a", "f"],
  "d": ["e"],
  "e": [],
  "f": ["b", "e"],
}) # -> ['c', 'a', 'f', 'b', 'd', 'e']

topological_order({
  "v": ["z", "w"],
  "w": [],
  "x": ["w", "v", "z"],
  "y": ["x"],
  "z": ["w"],
}) # -> ['y', 'x', 'v', 'z', 'w']
