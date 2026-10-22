class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return 0
        pos = nums.index(0)
        arr = nums[pos:]+nums[:pos]

        if arr == list(range(n)):
            return min(pos, n-pos+2)

        if arr == [0]+list(range(n-1,0,-1)):
            return min(n-pos,pos+2)
        return -1
