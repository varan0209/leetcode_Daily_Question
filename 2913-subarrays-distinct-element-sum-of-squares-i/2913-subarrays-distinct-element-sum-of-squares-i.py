class Solution(object):
    def sumCounts(self, nums):
        n = len(nums)
        res = 0
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                res += len(s) ** 2
        return res