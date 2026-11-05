from bisect import bisect_left

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2 = sorted(arr2)
        count = 0
        for a in arr1:
            i = bisect_left(arr2, a - d)       # first element >= a - d
            if i == len(arr2) or arr2[i] > a + d:
                count += 1                      # nothing in [a - d, a + d]
        return count