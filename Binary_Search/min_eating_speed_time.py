def minEatingSpeed(piles, h):
    # Helper function to check if Koko can finish all bananas at speed k within h hours
    def canFinish(k):
        hours = 0
        for pile in piles:
            # Calculate the number of hours needed for each pile at speed k
            # The formula (pile + k - 1) // k is equivalent to ceil(pile / k)
            hours += (pile + k - 1) // k
        # Check if the total hours needed is within the allowed hours h
        return hours <= h
    
    # Initialize the binary search boundaries
    left, right = 1, max(piles)
    
    # Perform binary search to find the minimum feasible eating speed k
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle point, which is our candidate for k
        if canFinish(mid):  # Check if Koko can finish with speed mid
            right = mid - 1  # If yes, try a smaller speed by moving the right boundary
        else:
            left = mid + 1  # If no, try a larger speed by moving the left boundary
    
    return left  # The left boundary will be the minimum feasible eating speed

# Test cases
print(minEatingSpeed([3, 6, 7, 11], 8))   # Output: 4
print(minEatingSpeed([30, 11, 23, 4, 20], 5))  # Output: 30
print(minEatingSpeed([30, 11, 23, 4, 20], 6))  # Output: 23