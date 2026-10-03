class Solution:
    def longestValidParentheses(self, s):

        stack = [-1]
        maxLength = 0

        for i, ch in enumerate(s):

            if ch == '(':

                stack.append(i)

            else:

                stack.pop()

                if not stack:

                    stack.append(i)

                else:

                    maxLength = max(maxLength, i - stack[-1])

        return maxLength