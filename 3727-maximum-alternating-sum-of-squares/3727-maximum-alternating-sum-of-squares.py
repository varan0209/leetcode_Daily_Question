class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sq = sorted((x * x for x in nums), reverse=True)
        plus = (len(sq) + 1) // 2   # number of positively-signed slots
        return sum(sq[:plus]) - sum(sq[plus:])