class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # cnt[b] = how many numbers have bit b set (bits 0..29 since nums[i] <= 1e9 < 2^30)
        cnt = [0] * 30
        for x in nums:
            for b in range(30):
                if (x >> b) & 1:
                    cnt[b] += 1

        ans = 0
        for _ in range(k):
            cur = 0
            for b in range(30):
                if cnt[b] > 0:
                    cur |= (1 << b)
                    cnt[b] -= 1
            ans = (ans + cur * cur) % MOD

        return ans