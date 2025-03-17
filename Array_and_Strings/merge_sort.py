from collections import deque

def merge_sort(nums):
  if len(nums) <= 1:
    return nums  
  mid_idx = len(nums) // 2
  left_sorted = merge_sort(nums[:mid_idx])
  right_sorted = merge_sort(nums[mid_idx:])  
  return merge(left_sorted, right_sorted)

def merge(list_1, list_2):
  list_1 = deque(list_1)
  list_2 = deque(list_2)
  
  merged = []
  while list_1 and list_2:
    if list_1[0] < list_2[0]:
      merged.append(list_1.popleft())
    else:
      merged.append(list_2.popleft())
  merged += list_1
  merged += list_2
  return merged

numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40]
merge_sort(numbers)
# -> [ 4, 5, 5, 6, 8, 10, 12, 40, 42, 100 ] 
# Time complexity: O(n log n)
# Space complexity: O(n)
# Where n is the length of the input list   # noqa: E501
numbers = [7, -30, -4, -1, 12, 0, 20]
merge_sort(numbers)
# -> [ -30, -4, -1, 0, 7, 12, 20 ] 
# Time complexity: O(n log n)
# Space complexity: O(n)
numbers = [
  72, 42, 16, 81, 84, 17,  2, 81, 22, 79, 86, 38, 
  77, 80, 81, 70, 81, 80, 35, 21, 89, 38, 57, 28, 
   4, 17, 50, 38, 68, 82, 22, 76, 45, 40, 67, 94, 
  37, 27, 81, 53, 36, 18, 28, 60, 45, 74, 40, 29, 
  18,  6, 28, 57, 42, 60, 64, 12, 78, 97, 96,  1, 
  20, 20, 61, 67, 82, 10, 63, 71, 39, 52, 37, 69, 
  37, 24, 66, 74, 15, 92, 49, 31, 56, 67, 50, 57, 
  79,  0, 21, 56, 82, 22,  4, 20, 91, 72, 58, 93, 
  99, 14, 42, 91 
]
merge_sort(numbers)
# -> [ 
#    0,  1,  2,  4,  4,  6, 10, 12, 14, 15, 16, 17, 
#   17, 18, 18, 20, 20, 20, 21, 21, 22, 22, 22, 24, 
#   27, 28, 28, 28, 29, 31, 35, 36, 37, 37, 37, 38, 
#   38, 38, 39, 40, 40, 42, 42, 42, 45, 45, 49, 50, 
#   50, 52, 53, 56, 56, 57, 57, 57, 58, 60, 60, 61, 
#   63, 64, 66, 67, 67, 67, 68, 69, 70, 71, 72, 72, 
#   74, 74, 76, 77, 78, 79, 79, 80, 80, 81, 81, 81, 
#   81, 81, 82, 82, 82, 84, 86, 89, 91, 91, 92, 93, 
#   94, 96, 97, 99 
# ]
# Time complexity: O(n log n)
# Space complexity: O(n)