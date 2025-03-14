from collections import Counter
def subarray_sum_count(numbers, target_sum):
  prefix_list = [0]
  total = 0
  count = 0
  seen = Counter()
  
  for num in numbers:
    # print(num)
    total += num
    prefix_list.append(total)
  print(prefix_list)
  for current in prefix_list:

    complement = current - target_sum
    count += seen[complement]
    seen[current] += 1
    print(seen)
  # print(count)
  return count


subarray_sum_count([-2, 1, 1, 1, -1, 1, 1, 1, 1], 3) # -> 8

