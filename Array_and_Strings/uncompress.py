def uncompress(s):
  numbers = '0123456789' #uncompress("2c3a1t") length is 6
  result = []
  i = 0
  j = 0
  while j < len(s): # 0 < 6
    if s[j] in numbers: #2
      j += 1
    else:
      num = int(s[i:j]) # num = int(s[2:c])
      result.append(s[j] * num) # S[C] * int(s[2:c]) cc
      j += 1
      i = j

  return ''.join(result)


"""
The uncompress function is designed to take a compressed string, where numbers indicate how many times the following character should be repeated, and return the uncompressed version. 

To start, we create a variable numbers containing all the digits from 0 to 9, and an empty list called result to store the expanded characters. We also initialize two index variables, i and j, both set to 0. The main idea is to iterate through the string using a while loop. If the current character at index j is a number, we increase j by 1 to move past the numbers to the next character. Once we encounter a non-numeric character, we know that the substring from index i to j represents the number of times this character should be repeated. We convert this substring into an integer, then append the character at j repeated num times to the result list. After that, we move j to the next character and update i to match j, so the next number can be tracked correctly. This process continues until the entire string is uncompressed. Finally, we join the result list into a single string and return it.

	1.	Initial Setup:
	•	We define numbers = '0123456789' to identify numeric characters.
	•	result = [] is an empty list where we’ll store the expanded characters.
	•	i = 0 and j = 0 are indices we’ll use to traverse the string.
	2.	Traversing the String:
	•	We use a while loop to iterate through the string s until j reaches the end of the string.
	•	The loop checks if the current character s[j] is a number. If it is, we increment j to continue looking for the next character (which isn’t a number).
  3.	Extracting the Number and Character:
	•	Once s[j] is not a number (i.e., it’s a character), we know that the substring s[i:j] contains the number that tells us how many times the character should be repeated.
	•	We convert this substring into an integer with num = int(s[i:j]).
	4.	Appending to the Result:
	•	We append the character s[j] repeated num times to the result list.
	•	Then, we increment j to move to the next part of the string and set i = j so that i is ready to track the start of the next number.
	5.	Final Output:
	•	After the loop completes, result contains all the expanded characters, and we use ''.join(result) to combine them into a single string, which is then returned.
"""


uncompress("2c3a1t") # -> 'ccaaat'
uncompress("4s2b") # -> 'ssssbb'
uncompress("2p1o5p") # -> 'ppoppppp'
uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'

