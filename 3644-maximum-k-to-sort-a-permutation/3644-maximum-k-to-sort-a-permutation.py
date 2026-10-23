class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = -1  # all bits set
        for i, v in enumerate(nums):
            if v != i:
                k &= v
        return 0 if k == -1 else k