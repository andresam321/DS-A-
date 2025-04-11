from collections import Counter

def intersection_with_dupes(a, b):
  count_a = Counter(a)
  count_b = Counter(b)
  result = []

  for ele in count_a:
    for i in range(0, min(count_a[ele], count_b[ele])):
      result.append(ele)

  return result

def intersection_with_dupes(a, b):
  obj_1 = {}
  obj_2 = {}
  result = []
  for ele in a:
    if ele not in obj_1:
      obj_1[ele] = 0
    obj_1[ele] += 1
  for ele in b:
    if ele not in obj_2:
      obj_2[ele] = 0
    obj_2[ele] += 1
#   print("1",obj_1)
#   print("2",obj_2)
  for key, value in obj_1.items():
    # print(key,value)
    if key in obj_2:
    #   print(key)
      times = min(obj_1[key], obj_2[key])
    #   print(times)
      for _ in range(times):
        result.append(key)
#   print(result)
          
  return result

intersection_with_dupes(
  ["a", "b", "c", "b"], 
  ["x", "y", "b", "b"]
) # -> ["b", "b"]
intersection_with_dupes(
  ["q", "b", "m", "s", "s", "s"], 
  ["s", "m", "s"]
) # -> ["m", "s", "s"]
intersection_with_dupes(
  ["p", "r", "r", "r"], 
  ["r"]
) # -> ["r"]
intersection_with_dupes(
  ["t", "v", "u"], 
  ["g", "e", "d", "f"]
) # -> [ ]
intersection_with_dupes(
  ["a", "a", "a", "a", "a", "a",], 
  ["a", "a", "a", "a"]
) # -> ["a", "a", "a", "a"]
