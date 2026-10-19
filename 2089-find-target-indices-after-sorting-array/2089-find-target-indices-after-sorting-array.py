class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less = 0
        count = 0
        for x in nums:
            if x < target:
                less += 1
            elif x == target:
                count += 1
        return list(range(less, less + count))