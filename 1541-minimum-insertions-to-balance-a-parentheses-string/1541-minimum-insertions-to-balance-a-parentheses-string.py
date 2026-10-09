class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_cnt = 0   # unmatched '(' so far
        ins = 0        # insertions made
        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                open_cnt += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    ins += 1      # insert a ')' to complete the pair
                    i += 1
                if open_cnt > 0:
                    open_cnt -= 1
                else:
                    ins += 1      # insert a '(' to match this '))'
        return ins + 2 * open_cnt