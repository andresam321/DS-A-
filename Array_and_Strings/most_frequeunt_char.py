def most_frequent_char(s):
    # Step 1: Create a dictionary to store the count of each character.
    # The keys will be the characters, and the values will be the count of occurrences.
    count = {}  

    # Step 2: Iterate through each character in the string `s`.
    for char in s:
        # Step 3: If the character is not already in the dictionary, initialize its count to 0.
        if char not in count:
            count[char] = 0
        # Step 4: Increment the count for the character by 1.
        count[char] += 1

    # Step 5: Find the character with the maximum count using `max`.
    # `key=count.get` tells `max` to compare dictionary values (counts) instead of keys.
    num = max(count, key=count.get)  

    # Step 6: Return the character with the highest count.
    return num
