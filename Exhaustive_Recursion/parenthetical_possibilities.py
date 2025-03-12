def parenthetical_possibilities(s):
  if len(s) == 0:
    return [""]
#  ('(mn)yz', 'x') 
  remaining, chars = get_options(s)
# ('(mn)yz', 'x')                        '(mn)yz'
  suffixes = parenthetical_possibilities(remaining)
  print(f"chars", chars)
  possibilities = []
  for char in chars:
    possibilities += [char + suffix for suffix in suffixes] 
  return possibilities

def get_options(s):
  if s[0] == "(":
    idx = s.index(")")
    chars = s[1:idx]
    remaining = s[idx + 1:]
    return (remaining, chars)
  else:
    chars = s[0]
    remaining = s[1:]
    return (remaining, chars)

print(parenthetical_possibilities('x(mn)yz')) # -> 
# [ 'xmyz', 'xnyz' ]