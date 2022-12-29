class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost1, cost2 = cost[0], cost[1]
        for i in range(len(cost) - 1):
            now_cost = cost[i] + min(cost1, cost2)
            cost1, cost2 = cost2, now_cost

        return min(cost1, cost2)

cost = [1,100,1,1,1,100,1,1,100,1]
a = Solution().minCostClimbingStairs(cost)
print(a)