#stack , lifo , last in first out
def dfs_iterative(graph, start):
    stack = [start]
    visited = set([start])

    while stack:
        node = stack.pop()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(dfs_iterative(graph, 'f'))