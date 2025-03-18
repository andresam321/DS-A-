def binary_search(numbers,target):
  lo = 0
  hi = len(numbers) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if target < numbers[mid]:
      hi = mid - 1
    elif target > numbers[mid]:
      lo = mid + 1
    else:
      return mid
  return -1 

binary_search([0, 6, 8, 12, 16, 19, 20, 28], 8) # -> 2
binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27) # -> -1
binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27) # -> -1
