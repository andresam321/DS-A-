def minimum_island(grid):
  visited = set()
  min_size = float("inf")
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if (row, col) not in visited and grid[row][col] == "L":
        size = explore(grid, row, col, visited)
        if size < min_size:
          min_size = size
  return min_size 

def explore(grid, row, col, visited):
  stack = [(row,col)]
  size = 0
  while stack:
    row, col = stack.pop()

    if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
      continue

    if grid[row][col] == "W":
      continue


    pos = (row,col)
    
    if pos in visited:
      continue
    visited.add(pos)

    size += 1
    stack.append((row - 1, col))
    stack.append((row + 1, col))
    stack.append((row, col - 1))
    stack.append((row, col + 1))

  return size


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid)) # -> 2


grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(minimum_island(grid)) # -> 1


grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

print(minimum_island(grid)) # -> 9


grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

print(minimum_island(grid)) # -> 1
