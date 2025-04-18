def is_palindrome(s):
  left = 0
  right = len(s) - 1
  while left < right:
    print(s[left], s[right])
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True

# def is_palindrome(s, left, right):
#     if left >= right:
#         return True
#     if s[left] != s[right]:
#         return False
#     return is_palindrome(s, left + 1, right - 1)
is_palindrome("pop") # -> True
is_palindrome("kayak") # -> True
is_palindrome("abcbca") # -> False
is_palindrome("abcbca") # -> False
