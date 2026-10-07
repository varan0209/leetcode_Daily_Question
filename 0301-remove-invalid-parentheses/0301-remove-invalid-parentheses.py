from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(t):
            bal = 0
            for ch in t:
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        if is_valid(s):
            return [s]

        visited = {s}
        queue = deque([s])
        result = []
        found = False

        while queue and not found:
            level_size = len(queue)
            for _ in range(level_size):
                cur = queue.popleft()
                for i in range(len(cur)):
                    if cur[i] not in '()':
                        continue
                    nxt = cur[:i] + cur[i+1:]
                    if nxt in visited:
                        continue
                    visited.add(nxt)
                    if is_valid(nxt):
                        result.append(nxt)
                        found = True
                    else:
                        queue.append(nxt)

        return result if found else [""]