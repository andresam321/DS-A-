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

heap = MinHeap()
heap.insert(12)
heap.insert(13)
heap.insert(11)
heap.insert(4)
heap.insert(20)
heap.insert(9)
heap.insert(22)
heap.insert(14)

#
#               4
#            /    \
#          11      9
#         / \    /  \
#       13  20  12  22
#      /
#    14
#
# [ 4, 11, 9, 13, 20, 12, 22, 14 ]

