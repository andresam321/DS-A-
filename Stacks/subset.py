def subsets(elements):
  if not elements:
    return [[]]

  first = elements[0]
  remaining_elements = elements[1:]
  subsets_without_first = subsets(remaining_elements)
  print(subsets_without_first)

  subsets_with_first = []
  for sub in subsets_without_first:
    subsets_with_first.append([first, *sub])
  return subsets_without_first + subsets_with_first


subsets(['a', 'b', 'c']) # -> [[], ['c'], ['b'], ['b', 'c'], ['a'], ['a', 'c'], ['a', 'b'], ['a', 'b', 'c']]
subsets(['q', 'r', 's', 't']) # ->
# [
#   [],
#   [ 't' ],
#   [ 's' ],
#   [ 's', 't' ],
#   [ 'r' ],
#   [ 'r', 't' ],
#   [ 'r', 's' ],
#   [ 'r', 's', 't' ],
#   [ 'q' ],
#   [ 'q', 't' ],
#   [ 'q', 's' ],
#   [ 'q', 's', 't' ],
#   [ 'q', 'r' ],
#   [ 'q', 'r', 't' ],
#   [ 'q', 'r', 's' ],
#   [ 'q', 'r', 's', 't' ]
# ]
