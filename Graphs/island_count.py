def island_count(grid):
    visited = set()
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited and grid[r][c] == 'L':  # Only explore unvisited land
              # 0 , 0
                if explore(grid, r, c, visited):
                    count += 1
    return count


#                 0   0
def explore(grid, r , c, visited):
  stack = [(r,c)]

  while stack:
    r, c = stack.pop()

    if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])):
      continue
    
    if grid[r][c] == "W":
      continue

    pos = (r,c)
    if pos in visited:
      continue
    visited.add(pos)

    stack.append((r - 1, c))  # Up
    stack.append((r + 1, c))  # Down
    stack.append((r, c - 1))  # Left
    stack.append((r, c + 1))  # Right
  return True

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

island_count(grid) # -> 3


grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

island_count(grid) # -> 4


grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

island_count(grid) # -> 1


grid = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
]

island_count(grid) # -> 0
