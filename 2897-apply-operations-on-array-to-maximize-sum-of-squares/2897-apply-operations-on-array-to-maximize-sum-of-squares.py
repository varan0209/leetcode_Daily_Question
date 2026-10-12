class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10 ** 9 + 7
        cnt = [0] * 31
        for x in nums:
            for b in range(31):
                if x >> b & 1:
                    cnt[b] += 1
        res = 0
        for _ in range(k):
            v = 0
            for b in range(31):
                if cnt[b]:
                    v |= 1 << b
                    cnt[b] -= 1
            res = (res + v * v) % MOD
        return res