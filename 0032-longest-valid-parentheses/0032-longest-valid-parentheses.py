class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                if len(stack) == 0:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_len = max(max_len, length)

        return max_len