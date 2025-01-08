def pair_sum(numbers, target_sum):
    # Step 1: Create an empty dictionary to store numbers we've seen so far and their indices.
    previous_numbers = {}  

    # Step 2: Loop through the list using `enumerate` to track both the index and the current number.
    for index, num in enumerate(numbers):
        # Step 3: Calculate the complement needed to reach the target sum.
        # complement = target_sum - num
        complement = target_sum - num  # Example: If target_sum = 8 and num = 3, then complement = 5

        # Step 4: Check if the complement is already in the dictionary.
        if complement in previous_numbers:
            # If the complement exists in `previous_numbers`, we've found a pair that adds to the target_sum.
            # Return the current index and the index of the complement from the dictionary.
            return (index, previous_numbers[complement])  # Example: (2, 0)

        # Step 5: If the complement is not found, store the current number and its index in `previous_numbers`.
        # This ensures we can look it up in future iterations.
        previous_numbers[num] = index  # Example: Add {3: 0}, {2: 1}, {5: 2}, etc.

    # If no pair is found after the loop, return None (this case won't occur if the problem guarantees a solution).
    return None


# Example usage and explanation:
numbers = [3, 2, 5, 4, 1]
target_sum = 8

# Call the function and print the result
result = pair_sum(numbers, target_sum)

# Output should be (2, 0) because 5 (index 2) + 3 (index 0) = 8
print(f"The indices of the numbers that sum to {target_sum} are: {result}")
