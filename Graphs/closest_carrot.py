from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  visited = set([ (starting_row, starting_col) ])
  queue = deque([ (starting_row, starting_col, 0 ) ])

  while queue:
    row, col , distance = queue.popleft()

    if grid[row][col] == "C":
      return distance

    deltas = [(1,0), (-1,0), (0,1), (0, -1)]

    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = row + delta_row
      neighbor_col = col + delta_col
      pos = (neighbor_row, neighbor_col)
      row_inbounds = 0 <= neighbor_row < len(grid)
      col_inbounds = 0 <= neighbor_col < len(grid[0])
      print(row_inbounds, col_inbounds)
      if row_inbounds and col_inbounds and pos not in visited and grid[neighbor_row][neighbor_col] != "X":
        visited.add(pos)
        queue.append((neighbor_row, neighbor_col, distance + 1))
  return -1


grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

closest_carrot(grid, 1, 2) # -> 4


grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

closest_carrot(grid, 0, 0) # -> 5


grid = [
  ['O', 'O', 'X', 'X', 'X'],
  ['O', 'X', 'X', 'X', 'C'],
  ['O', 'X', 'O', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'C', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O'],
]

closest_carrot(grid, 3, 4) # -> 9


grid = [
  ['O', 'O', 'X', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'O'],
  ['O', 'X', 'C', 'C', 'O'],
]

closest_carrot(grid, 1, 4) # -> 2


grid = [
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'C'],
]

closest_carrot(grid, 0, 0) # -> -1


grid = [
  ['O', 'O', 'X', 'C', 'O'],
  ['O', 'X', 'X', 'X', 'O'],
  ['C', 'X', 'O', 'O', 'O'],
];

closest_carrot(grid, 2, 2) # -> 5
