class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        t = sorted(s)
        if list(s) == t:
            return 0
        if n == 2:
            return -1

        # first / last positions that differ from the sorted string
        l = 0
        while s[l] == t[l]:
            l += 1
        r = n - 1
        while s[r] == t[r]:
            r -= 1
        if l > 0 or r < n - 1:
            return 1  # sort exactly s[l..r], a proper substring

        # need to touch the whole span, so use two overlapping proper sorts if possible
        lo, hi = t[0], t[-1]
        min_ok = s.find(lo) < n - 1   # global min exists in s[0..n-2]
        max_ok = s.rfind(hi) > 0      # global max exists in s[1..n-1]
        if min_ok or max_ok:
            return 2
        return 3