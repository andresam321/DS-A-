def prereqs_possible(num_courses, prereqs):
# here we call the build graph function to build the graph that was build
  graph = build_graph(num_courses, prereqs)
  print(graph)
# we have to sets for white grey black algo
# white being not visited, grey being visting, and black being visited
  visiting = set()
  visited = set()
# then we iterate through each node from ranging 0 , to the current number of courses 
  for node in range(0, num_courses):
    # then we check the cycle detect helper function
    # print(f"node",node)
  #          graph i built, 0
    if cycle_detect(graph,node, visiting, visited):
      return False

  return True

def cycle_detect(graph, node, visiting, visited):
  if node in visited:
    return False
  if node in visiting:
    return True
# 0 is not in visited or hasnt been visiting  so we add it to the visiting 
  visiting.add(node)
# here we iterate through the neighbors of each node starting at 0
    
  for neighbor in graph[node]:
    # print(f"graph[node]", graph[node])
  #           visting             {3,2,1,0}

    if cycle_detect(graph, neighbor, visiting, visited):
      return True
  visiting.remove(node)
  visited.add(node)
  
  return False

def build_graph(num_courses, prereqs):
  graph = {}
# this will looop from 0 all the way to num courses - 1 since where checking how many num courses it requires
  for i in range(0, num_courses):
# adding each individual each course up to num_course as a key - 1
    graph[i] = []
  # print(graph)
# then we iterate through each tuple m
  for prereq in prereqs:
  # we decompress the tuple assigning each with a , and b 
    a, b = prereq
  # then we append each prereq into the corresponding key to see which are the requirements for each prereq
    graph[a].append(b)
  # print(graph)
  return graph



numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
prereqs_possible(numCourses, prereqs) # -> True

numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
  (3, 0),
]
prereqs_possible(numCourses, prereqs) # -> False

numCourses = 5
prereqs = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
]
prereqs_possible(numCourses, prereqs) # -> True

numCourses = 6
prereqs = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
  (5, 3),
  (3, 5),
]
prereqs_possible(numCourses, prereqs) # -> False

numCourses = 8
prereqs = [
  (1, 0),
  (0, 6),
  (2, 0),
  (0, 5),
  (3, 7),
  (4, 3),
]
prereqs_possible(numCourses, prereqs) # -> True

numCourses = 8
prereqs = [
  (1, 0),
  (0, 6),
  (2, 0),
  (0, 5),
  (3, 7),
  (7, 4),
  (4, 3),
]
prereqs_possible(numCourses, prereqs) # -> False
numCourses = 42
prereqs = [(6, 36)]
prereqs_possible(numCourses, prereqs) # -> True
