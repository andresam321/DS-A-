def rare_routing(n, roads):
    # Build the graph using the helper function
    graph = make_graph(n, roads)
    print(graph)  # Optional: helps you see the graph structure

    # Set to keep track of visited nodes
    visited = set()

    # Start DFS from node 0
    valid = validate(graph, 0, visited, None)

    # Return True only if:
    # - The DFS confirms no cycles (valid == True)
    # - All nodes were visited (graph is connected)
    return valid and len(visited) == n


def validate(graph, node, visited, last_node):
    # If we've already visited this node, we found a cycle
    if node in visited:
        return False

    # Mark the current node as visited
    visited.add(node)

    # Explore all neighbors of the current node
    for neighbor in graph[node]:
        # Skip the node we just came from to avoid false cycle detection
        if neighbor != last_node:
            # Recursively visit the neighbor
            # If it returns False (cycle found), return False immediately
            if not validate(graph, neighbor, visited, node):
                return False

    # If all neighbors are valid, return True
    return True


def make_graph(n, roads):
    # Initialize a graph where each node maps to a list of neighbors
    graph = {}

    # Create an empty list for each city
    for city in range(n):
        graph[city] = []

    # Add connections (edges) for each undirected road
    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)

    return graph

rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3)
]) # -> True

rare_routing(6, [
  (1, 2),
  (4, 1),
  (5, 4),
  (3, 0),
  (0, 1),
  (0, 4),
]) # -> False
rare_routing(5, [
  (0, 1),
  (0, 2),
  (0, 3),
  (0, 4),
]) # -> True