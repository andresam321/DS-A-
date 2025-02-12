from collections import deque

def knight_attack(n, kr, kc, pr, pc):
  visited = set();
  visited.add((kr, kc))
  queue = deque([ (kr, kc, 0) ])
  while len(queue) > 0:
    r, c, step = queue.popleft();
    if (r, c) == (pr, pc):
      return step
    neighbors = get_knight_moves(n, r, c)
    for neighbor in neighbors:
      neighbor_row, neighbor_col = neighbor
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor_row, neighbor_col, step + 1))
  return None

def get_knight_moves(n, r, c):
  positions = [
    ( r + 2, c + 1 ),
    ( r - 2, c + 1 ),
    ( r + 2, c - 1 ),
    ( r - 2, c - 1 ),
    ( r + 1, c + 2 ),
    ( r - 1, c + 2 ),
    ( r + 1, c - 2 ),
    ( r - 1, c - 2 ),
  ]
  inbounds_positions = [];
  for pos in positions:
    new_row, new_col = pos
    if 0 <= new_row < n and 0 <= new_col < n:
      inbounds_positions.append(pos)
  return inbounds_positions
knight_attack(8, 1, 1, 2, 2) # -> 2
knight_attack(8, 1, 1, 2, 3) # -> 1
knight_attack(8, 0, 3, 4, 2) # -> 3
knight_attack(8, 0, 3, 5, 2) # -> 4
knight_attack(24, 4, 7, 19, 20) # -> 10
