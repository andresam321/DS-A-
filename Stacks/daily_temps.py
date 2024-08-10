# https://leetcode.com/problems/daily-temperatures/description/
# https://neetcode.io/problems/daily-temperatures

# Daily Temps
# Given an array of integers representing daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100

# Example 4:
# Input: [80,70,60,50,40]
# Output: [0,0,0,0,0]


# input = [73,74,75,71,69,72,76,73]

# res = [1,1,4,2,1,1,0,0]

# stack = [76,73]


# Pseudocode:
# Create an array called result and fill it with all zeros
# Use a stack
# Iterate over temps
# On each iteration
# While the current temp is > prev temp on top of stack
# pop the stack and update the result by taking the curr index and subtracting the prev temp's index
# push on the current temp and its index to the stack
# return the result at the end

# input [73,72,71,70,69,90]

# input = [73,74,75,71,69,72,76,73]

# res = [1,1,4,2,1,1,0,0]

# stack = [[76,6],[73,7]]

# Time O(n)
# Space O(n)

# const dailyTemps = temps => {
# 	const res = new Array(temps.length).fill(0);
# 	const stack = [];	
# 	for (let i = 0; i < temps.length; i++) {//O(n)
# 	let currTemp = temps[i]; //73
# 	while(stack.length && currTemp > stack[stack.length -1][0]){
# 	let [prevTemp, prevTempIndex] = stack.pop(); // 69, 4
# 	res[prevTempIndex] = i - prevTempIndex;
# }
# stack.push([currTemp, i])
# }
# return res;
# };
