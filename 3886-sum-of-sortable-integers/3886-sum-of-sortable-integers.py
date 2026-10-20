from bisect import bisect_left

class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # D = indices j where nums[j] > nums[j+1]
        D = [j for j in range(n - 1) if nums[j] > nums[j + 1]]

        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            prev_max = 0
            for s in range(0, n, k):
                e = s + k - 1
                # internal descents in [s, e-1]
                lo = bisect_left(D, s)
                hi = bisect_left(D, e)
                cnt = hi - lo
                if cnt >= 2:
                    ok = False
                    break
                if cnt == 1:
                    j = D[lo]
                    if nums[e] > nums[s]:   # wrap would be a second descent
                        ok = False
                        break
                    bmin, bmax = nums[j + 1], nums[j]
                else:
                    bmin, bmax = nums[s], nums[e]
                if bmin < prev_max:
                    ok = False
                    break
                prev_max = bmax
            if ok:
                total += k
        return total