def grocery_budget(grocery_list, budget):
    print(f"\nCALL: grocery_list={grocery_list}, budget={budget}")

    if budget < 0:
        print("→ Over budget! Returning []")
        return []

    if not grocery_list:
        print("→ Reached end of list. Returning [[]]")
        return [[]]

    all_lists = []
    current_item_name, current_item_price = grocery_list[0]

    print(f"Including '{current_item_name}' (cost: {current_item_price})")
    for list_with_current_item in grocery_budget(grocery_list[1:], budget - current_item_price):
        list_with_current_item.append(current_item_name)
        all_lists.append(list_with_current_item)

    print(f"Excluding '{current_item_name}'")
    lists_without_current_item = grocery_budget(grocery_list[1:], budget)
    all_lists += lists_without_current_item

    print(f"Returning from list: {grocery_list} → {all_lists}")
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
