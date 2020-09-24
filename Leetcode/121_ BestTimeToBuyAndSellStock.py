import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min = sys.maxsize
        for a in prices:
            if result < a - min:
                result = a - min
            if a < min:
                min = a
        return result