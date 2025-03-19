def lexical_order(word_1, word_2, alphabet):
  length = max(len(word_1), len(word_2))
  print(length)
  for i in range(length):
    value_1 = alphabet.index(word_1[i]) if i < len(word_1) else float("-inf")
    value_2 = alphabet.index(word_2[i]) if i < len(word_2) else float("-inf")
    if value_1 < value_2:
      return True
    elif value_2 < value_1:
      return False
  return True
# index     0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 
alphabet = "a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z "
lexical_order("apple", "dock", alphabet) # -> True
lexical_order("apple", "app", alphabet) # -> False
lexical_order("apple", "apple", alphabet) # -> True
lexical_order("apple", "apple", alphabet) # -> True