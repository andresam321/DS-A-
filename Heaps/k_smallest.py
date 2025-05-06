import heapq

def k_smallest(nums, k):
  max_heap = []

  for v in nums:
    item = (-v, v)
    heapq.heappush(max_heap, item)
    if len(max_heap) > k:
      heapq.heappop(max_heap)
    # print(max_heap)
  result = []
  while len(max_heap) > 0:
    item = heapq.heappop(max_heap)
    result.append(item[1])
  # print(result[::-1])    
  return result[::-1]


k_smallest([8, 2, 7, -3, 5, 10], 3) 
# -> [-3, 2, 5]

k_smallest([84, 22, 52, 69, 71, 22, 88, 100, 13, 89, 79], 4) 
# -> [13, 22, 22, 52]


k_smallest([
  43, 35, 62, 31, 86, 81, 58, 80, 91, 13, 54, 78, 
  75, 69, 60, 8, 22, 12, 30, 79, 100, 2, 64, 57, 
  11, 55, 7, 68, 66, 14, 45, 26, 83, 24, 28, 76, 
  34, 89, 37, 32, 41, 88, 20, 82, 59, 4, 40, 9, 
  74, 23
], 5)
# -> [2, 4, 7, 8, 9]
