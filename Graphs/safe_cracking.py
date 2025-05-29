def safe_cracking(hints):
  in_degree = {}
  graph = build_graph(hints)
  # print(in_degree)
  for node in graph:
    in_degree[node] = 0
  print(in_degree)
  for node in graph:
    for child in graph[node]:
      in_degree[child] += 1
  print(in_degree)
  hint = [ node for node in graph if in_degree[node] == 0]
  order = ''
  while hint:
    node = hint.pop()
    order += str(node)
    for child in graph[node]:
      in_degree[child] -= 1
      if in_degree[child] == 0:
        hint.append(child)
  return order
def build_graph(edges):
  graph = {}
  for edge in edges:
    # print(edge)
    a , b = edge

    if not a in graph:
      graph[a] = []
    if not b in graph:
      graph[b] = []

    graph[a].append(b)
  return graph
safe_cracking([
  (3, 1),
  (4, 7),
  (5, 9),
  (4, 3),
  (7, 3),
  (3, 5),
  (9, 1),
]) # -> '473591'