class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        j = 0
        for key in nums:
            if a.get(key) is None:
                a[key] = [j]
            else:
                a[key].append(j)
            j = j + 1
        for item in a:
            remain = target - item
            remain_value = a.get(remain)
            if remain_value is not None:
                ans_1 = a.get(item)[0]
                ans_2 = remain_value[-1]
                
                if ans_1 != ans_2:
                    return [a.get(item)[0], remain_value[-1]]