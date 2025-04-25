def kth_largest(numbers, k):
  sorted_numbers = sorted(numbers)
  return sorted_numbers[-k]

class MinHeap:
  def __init__(self):
    self.list = []
    
  def is_empty(self):
    return len(self.list) == 0

  def size(self):
    return len(self.list)
  
  def swap(self, index_1, index_2):
    self.list[index_1], self.list[index_2] = self.list[index_2], self.list[index_1]
  
  def sift_up(self, index):
    current_index = index
    while current_index > 0:
      parent_index = (current_index - 1) // 2
      if self.list[current_index] < self.list[parent_index]:
        self.swap(current_index, parent_index)
        current_index = parent_index
      else:
        break
    
  def insert(self, val):
    self.list.append(val)
    self.sift_up(self.size() - 1)
      
  def sift_down(self, index):
    current_index = index
    while current_index < self.size() - 1:
      left_child_index = current_index * 2 + 1
      right_child_index = current_index * 2 + 2
      
      left_child_val = float("inf") if left_child_index >= self.size() else self.list[left_child_index]
      right_child_val = float("inf") if right_child_index >= self.size() else self.list[right_child_index]
      
      smaller_child_val = left_child_val if left_child_val < right_child_val else right_child_val
      smaller_child_index = left_child_index if left_child_val < right_child_val else right_child_index
      
      if self.list[current_index] > smaller_child_val:
        self.swap(current_index, smaller_child_index)
        current_index = smaller_child_index
      else:
        break
      
  def extract_min(self):
    if self.is_empty():
      return None
    
    if self.size() == 1:
      return self.list.pop()
    
    min_val = self.list[0]
    self.list[0] = self.list.pop()
    self.sift_down(0)
    return min_val

def kth_largest(numbers, k):
  heap = MinHeap()
  for num in numbers:
    #   print(num)
      heap.insert(num)
      if heap.size() > k:
          heap.extract_min()   
  
  result = heap.extract_min()
  print("K-th largest:", result)
  return result

import heapq

def kth_largest(numbers, k):
  heap = []
  for num in numbers:
    heapq.heappush(heap, num)
    if len(heap) > k:
      heapq.heappop(heap)
  return heapq.heappop(heap)

print(kth_largest([9,2,6,6,1,5,8,7], 3)) # -> 7
numbers = [  
  4,5,85,77,47,80,37,42,3,6,62,33,69,68,16,20,83,39,14,58,75,35,72,36,19,18,66,61,41,79,28,43,7,24,40,53,32,12
]
kth_largest(numbers, 9) # -> 68
numbers = [  
  4,5,85,77,47,80,37,42,3,6,62,33,69,68,16,20,83,39,14,58,75,35,72,36,19,18,66,61,41,79,28,43,7,24,40,53,32,12
]
kth_largest(numbers, 9) # -> 68
