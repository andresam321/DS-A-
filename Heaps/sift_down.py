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
      print(left_child_val)
      print(right_child_val)
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


heap = MinHeap()
heap.insert(12)
heap.insert(93)
heap.insert(63)
heap.insert(16)
heap.extract_min() # -> 12
heap.extract_min() # -> 16
heap.insert(-500)
heap.insert(21)
heap.insert(11)
heap.insert(43)
heap.insert(-6)
heap.insert(35)
heap.insert(15)
heap.extract_min() # -> -500
heap.extract_min() # -> -6
heap.extract_min() # -> 11
heap.extract_min() # -> 15
heap.extract_min() # -> 21
heap.extract_min() # -> 35
heap.extract_min() # -> 43
heap.extract_min() # -> 63
heap.extract_min() # -> 93
