def combine_intervals(intervals):
  sorted_intervals = sorted(intervals, key=lambda x : x[0])
  print(sorted(intervals, key=lambda x : x[0] ))
  combined = [ sorted_intervals[0] ]
#   print(sorted_intervals)
#   print(combined)
  
  for current_interval in sorted_intervals[1:]:
    last_start, last_end = combined[-1]
    current_start, current_end = current_interval
    
    if current_start <= last_end:
      if current_end > last_end:
        combined[-1] = (last_start, current_end)
    else:
      combined.append(current_interval)
      
  return combined

intervals = [
  (1, 4),
  (12, 15),
  (3, 7),
  (8, 13),
]
print(combine_intervals(intervals))
# -> [ (1, 7), (8, 15) ]
