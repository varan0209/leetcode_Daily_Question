class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        mx = max(diffs)
        cnt = [0] * (mx + 1)
        for d in diffs:
            cnt[d] += 1

        # shave the largest differences down, level by level
        for d in range(mx, 0, -1):
            if k == 0:
                break
            c = cnt[d]
            if c == 0:
                continue
            if k >= c:
                k -= c
                cnt[d - 1] += c
                cnt[d] = 0
            else:
                cnt[d] -= k
                cnt[d - 1] += k
                k = 0

        return sum(c * d * d for d, c in enumerate(cnt))