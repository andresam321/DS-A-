def exclusive_items(a, b):
  comb_list = {}
  result = []
  combine_list = a + b
  # print(combine_list)
  for ele in combine_list:
 
    if ele not in comb_list:
      comb_list[ele] = 0
    comb_list[ele] += 1
  item = comb_list.items()
  for key, value in item:
    if value == 1:
      result.append(key)
  return result

exclusive_items([4,2,1,6], [3,6,9,2,10]) # -> [4,1,3,9,10]

def exclusive_items(a, b):
  difference = []
  
  for item in a:
    if item not in b:
      difference.append(item)

  for item in b:
    if item not in a:
      difference.append(item)

  return difference

def exclusive_items(a, b):
  difference = []
  set_a = set(a)
  set_b = set(b)
  
  for item in a:
    if item not in set_b:
      difference.append(item)

  for item in b:
    if item not in set_a:
      difference.append(item)

  return difference

exclusive_items([2,4,6], [4,2]) # -> [6]
exclusive_items([0,1,2], [10,11]) # -> [0,1,2,10,11]
