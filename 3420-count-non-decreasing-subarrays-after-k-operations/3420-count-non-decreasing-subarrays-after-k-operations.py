from collections import deque

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        seg = deque()          # segments [level, count], left to right; level = prefix max of those elements
        cost = 0               # ops needed to make nums[l..r] non-decreasing
        r = n - 1
        total = 0
        for l in range(n - 1, -1, -1):
            x = nums[l]
            # add nums[l] on the left: elements before the next value >= x get raised to x
            cnt = 1
            while seg and seg[0][0] <= x:
                lv, c = seg.popleft()
                cost += (x - lv) * c
                cnt += c
            seg.appendleft([x, cnt])
            # shrink from the right until affordable
            while cost > k:
                top = seg[-1]
                cost -= top[0] - nums[r]
                top[1] -= 1
                if top[1] == 0:
                    seg.pop()
                r -= 1
            total += r - l + 1
        return total 