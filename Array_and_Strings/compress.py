def compress(s): #compress('ssssbbz') # -> '4s2bz'
  if not s:
    return ""
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[i] == s[j]: #s[0] == s[4]
      j += 1
    else:
      num = j - i #4- 0  = 4 
      if num == 1:
        result.append(s[i])
      else:
        result.append(str(num)) #4
        result.append(s[i]) # s
      i = j
      # result 4s
  return ''.join(result)

      
compress('ccaaatsss') # -> '2c3at3s'
 

"""
	1.	Initial Setup:
	•	First, we append an exclamation mark '!' to the end of the string s. This character acts as a sentinel, ensuring that the last group of characters in the string is processed correctly.
	•	We then create an empty list result to store the compressed form of the string.
	•	Two variables, i and j, are initialized to 0. These will be used to track the start and current position of a sequence of identical characters.
	2.	Iterating Through the String:
	•	We use a while loop that runs until j reaches the length of the string s.
	•	The first check in the loop, if s[i] == s[j], compares the characters at positions i and j.
	•	If s[i] == s[j], it means that the characters are the same, so we increment j by 1 to continue checking the next character in the sequence.
	•	We keep doing this until s[i] != s[j], which indicates the end of the current sequence of identical characters.
	3.	Processing the Sequence:
	•	Once we find that s[i] != s[j], we calculate the number of times the character s[i] appeared by taking num = j - i.
	•	If num == 1, it means the character appeared only once, so we just append the character itself to the result list.
	•	If num > 1, it means the character appeared multiple times, so we append str(num) (the count) followed by the character s[i] to the result list.
  	4.	Updating Indices:
	•	After processing the sequence, we set i = j to move i to the start of the next sequence of identical characters, and the loop continues.
	5.	Final Output:
	•	After the loop completes, result contains the compressed form of the string. We use ''.join(result) to combine the list elements into a single string and return it.
"""