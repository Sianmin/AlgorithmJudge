class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        before = 0
        sums = []
        for i in nums:
            sums.append(i + before)
            before = i + before
        return sums
        