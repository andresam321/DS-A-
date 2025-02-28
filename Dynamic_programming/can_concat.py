def can_concat(s, words):
  return _can_concat(s, words, {})

def _can_concat(s, words, memo):
  if s in memo:
    return memo[s]
  
  if s == '':
    return True
  
  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      if _can_concat(suffix, words, memo) == True:
        memo[s] = True
        return True
      
  memo[s] = False
  return False
can_concat("oneisnone", ["one", "none", "is"]) #  -> True
can_concat("oneisnone", ["on", "e", "is"]) #  -> False
can_concat("foodisgood", ["is", "g", "ood", "f"]) #  -> True
can_concat("santahat", ["santah", "san", "hat", "tahat"]) #  -> True
can_concat("rrrrrrrrrrrrrrrrrrrrrrrrrrx", ["r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"]) #  -> False
