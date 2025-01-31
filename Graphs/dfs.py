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