class Solution:

    def sortPermutation(self, n):
        r = -1
        for i, x in enumerate(n):
            if i != x:
                r &= x
        return max(r, 0)