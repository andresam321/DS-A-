def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1, {})

def _max_palin_subsequence(string, i, j, memo):
  key = (i, j)
  
  if key in memo:
    return memo[key]
  
  if i == j:
    return 1
  
  if i > j:
    return 0
  
  if string[i] == string[j]:
    memo[key] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
  else:
    memo[key] = max(
      _max_palin_subsequence(string, i + 1, j, memo),
      _max_palin_subsequence(string, i, j - 1, memo)
    )
    
  return memo[key]
max_palin_subsequence("luwxult") # -> 5
max_palin_subsequence("xyzaxxzy") # -> 6
max_palin_subsequence("abdbca") # -> 5
max_palin_subsequence("chartreusepugvicefree") # -> 7
max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty") # -> 15
max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe") # -> 31
