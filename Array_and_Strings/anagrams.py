def anagrams(s1, s2):
    # Compare the character counts of both strings to check if they are anagrams
    return char_count(s1) == char_count(s2)

def char_count(s):
    # Initialize an empty dictionary to store character counts
    count = {}
    
    for char in s:  # Iterate through each character in the string
        if char not in count:  # If the character is not in the dictionary, initialize it with 0
            count[char] = 0
        count[char] += 1  # Increment the count for the character
    
    return count  # Return the dictionary of character counts
### test cases


# anagrams('restful', 'fluster') # -> True
# anagrams('cats', 'tocs') # -> False
# anagrams('monkeyswrite', 'newyorktimes') # -> True
