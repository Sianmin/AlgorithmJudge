class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        F = [0, 0]
        for i in range(2, len(cost) + 1) :
            F.append(min(F[i-1] + cost[i-1], F[i-2] + cost[i-2]))
        return F[-1]