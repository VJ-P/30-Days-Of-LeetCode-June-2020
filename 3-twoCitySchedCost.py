# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

# Example 1:
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.

# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

# Note:
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)//2
        diff = {}
        for i in range(len(costs)):
            diff[i] = abs(costs[i][0]-costs[i][1])
        sortedDiff = sorted(diff.items(), key=lambda x: x[1], reverse=True)
        A = 0
        B = 0
        totalCost = 0
        for key in sortedDiff:
            person = key[0]
            if A < N and B < N:
                location = 0 if costs[person][0] < costs[person][1] else 1
                totalCost += costs[person][location]
                if location == 0:
                    A += 1
                else:
                    B += 1
            elif A < N:
                totalCost += costs[person][0]
                A += 1
            elif B < N:
                totalCost += costs[person][1]
                B += 1
        return totalCost
        