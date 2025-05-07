def grocery_budget(grocery_list, budget):
  
  if budget < 0:
    return []

  if not grocery_list:
    return [[]]

  all_lists = []
  
  current_item_name, current_item_price = grocery_list[0]
  # print(grocery_list[0])
  # print(current_item_price)
  for list_with_current_item in grocery_budget(grocery_list[1:], budget - current_item_price):
    list_with_current_item.append(current_item_name)
    all_lists.append(list_with_current_item)

  lists_without_current_item = grocery_budget(grocery_list[1:], budget)
  all_lists += lists_without_current_item
  
  return all_lists

grocery_budget([  
  ('eggs', 5),
  ('milk', 3),
  ('butter', 3)
], 7) # ->
# [ 
#   [ 'eggs' ], 
#   [ 'butter', 'milk' ], 
#   [ 'milk' ], 
#   [ 'butter' ], 
#   [] 
# ] 
