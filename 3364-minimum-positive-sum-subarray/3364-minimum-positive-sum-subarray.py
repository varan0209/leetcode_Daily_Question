class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, v in enumerate(nums):
            prefix[i + 1] = prefix[i] + v

        best = float('inf')
        for i in range(n):
            for length in range(l, r + 1):
                j = i + length
                if j > n:
                    break
                s = prefix[j] - prefix[i]
                if 0 < s < best:
                    best = s
        return best if best != float('inf') else -1