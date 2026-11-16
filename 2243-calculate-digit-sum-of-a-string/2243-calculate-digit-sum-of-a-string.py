class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            s = ''.join(str(sum(int(c) for c in s[i:i + k])) for i in range(0, len(s), k))
        return s