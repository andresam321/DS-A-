def intersection(a,b):
  new_list = []
  first_list = set()

  for item in a:
    first_list.add(item)

  for item in b:
    if item in first_list:
      new_list.append(item)

  return new_list

"""
We create first_list as a set to store unique elements from the list a. By using a set, we ensure that each item appears only once.
We then loop through the second list b. For each item in b, we check if it exists in the first_list set.
If the item is found in the set, we append it to the new_list because it means that item is common to both a and b.
The result is a list (new_list) containing the intersection of both lists, meaning it only includes items that are present in both a and b.

""" 

intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
intersection([2,4,6], [4,2]) # -> [2,4]
intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
intersection([0,1,2], [10,11]) # -> []
intersection([0,1,2], [10,11]) # -> []
