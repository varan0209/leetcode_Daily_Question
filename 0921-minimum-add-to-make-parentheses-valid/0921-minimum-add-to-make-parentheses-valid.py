class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_count = 0   # unmatched '(' seen so far
        add = 0          # insertions needed for unmatched ')'

        for ch in s:
            if ch == '(':
                open_count += 1
            else:  # ch == ')'
                if open_count > 0:
                    open_count -= 1
                else:
                    add += 1

        return add + open_count