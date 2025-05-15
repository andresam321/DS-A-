

def tolerant_teams(rivalries):
  graph = build_graph(rivalries)

  teams = {}
  for node in graph:
    print(node)
    if node not in teams:
      if not valid(graph, node, teams, False ):
        return False
  return True
# todo


def valid(graph,  node , teams, current_color):
  if node in teams:
    return current_color == teams[node]
  teams[node] = current_color
  for neighbor in graph[node]:
    print(neighbor)
    if not valid(graph, neighbor, teams, not current_color):
      return False
  return True
  

def build_graph(edges):
  graph = {}

  for edge in edges:
    a , b = edge

    if not a in graph:
      graph[a] = []
    if not b in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

  return graph

tolerant_teams([
  ('cindy', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt')
]) # -> True
tolerant_teams([
  ('cindy', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt'),
  ('brando', 'anj')
]) # -> False
tolerant_teams([
  ('raj', 'nader'),
  ('philip', 'seb'),
  ('raj', 'philip')
]) # -> False
tolerant_teams([
  ('raj', 'nader'),
  ('philip', 'seb'),
  ('raj', 'philip'),
  ('raj', 'seb')
]) # -> False
tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader')
]) # -> True
