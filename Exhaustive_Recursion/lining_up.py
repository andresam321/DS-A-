def lining_up(people, capacity):
  if capacity > len(people):
    return []

  if capacity == 0:
    return [[]]

  all_lines = []
  
  current_person = people[0]
  remaining_people = people[1:]
  
  for line in lining_up(remaining_people, capacity - 1):
    for i in range(0, len(line) + 1):
      line_with_current = [ *line[:i], current_person, *line[i:] ]
      all_lines.append(line_with_current)

  for line_without_current in lining_up(remaining_people, capacity):
    all_lines.append(line_without_current)

  return all_lines


def lining_up(people, capacity):
  peeps_list = []
  if capacity == 0:
    return [[]]
  for i in range(len(people)):
    person = people[i]
    rest = people[:i] + people[i+1:]
    for sub_line in lining_up(rest, capacity - 1):
      peeps_list.append([person] + sub_line)
  print(peeps_list)
  return peeps_list

lining_up(["jason", "jen", "cody", "vicky"], 3) # ->
# [ 
#   [ 'jason', 'jen', 'cody' ], 
#   [ 'jen', 'jason', 'cody' ], 
#   [ 'jen', 'cody', 'jason' ], 
#   [ 'jason', 'cody', 'jen' ], 
#   [ 'cody', 'jason', 'jen' ], 
#   [ 'cody', 'jen', 'jason' ], 
#   [ 'jason', 'jen', 'vicky' ], 
#   [ 'jen', 'jason', 'vicky' ], 
#   [ 'jen', 'vicky', 'jason' ], 
#   [ 'jason', 'vicky', 'jen' ], 
#   [ 'vicky', 'jason', 'jen' ], 
#   [ 'vicky', 'jen', 'jason' ], 
#   [ 'jason', 'cody', 'vicky' ], 
#   [ 'cody', 'jason', 'vicky' ], 
#   [ 'cody', 'vicky', 'jason' ], 
#   [ 'jason', 'vicky', 'cody' ], 
#   [ 'vicky', 'jason', 'cody' ], 
#   [ 'vicky', 'cody', 'jason' ], 
#   [ 'jen', 'cody', 'vicky' ], 
#   [ 'cody', 'jen', 'vicky' ], 
#   [ 'cody', 'vicky', 'jen' ], 
#   [ 'jen', 'vicky', 'cody' ], 
#   [ 'vicky', 'jen', 'cody' ], 
#   [ 'vicky', 'cody', 'jen' ] 
# ] 
