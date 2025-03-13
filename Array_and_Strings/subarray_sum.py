def has_subarray_sum(numbers, target_sum):
  prefix_sums = [0]
  total = 0
  for num in numbers:
    total += num
    prefix_sums.append(total)
  print(prefix_sums)
  seen = set()
  for current in prefix_sums:
    complement = current - target_sum
    if complement in seen:
      return True
    seen.add(current)
  return False

has_subarray_sum([1, 3, 1, 4, 3], 8) # -> True
has_subarray_sum([1, 3, 1, 4, 3], 2) # -> False
has_subarray_sum([1, 3, 1, 4, 3], 7) # -> True      