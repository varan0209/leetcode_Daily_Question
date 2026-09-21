class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        cnt = [0] * k  # cnt[t] = # subarrays ending at previous index with product % k == t

        for num in nums:
            r = num % k
            new_cnt = [0] * k
            for t in range(k):
                if cnt[t]:
                    new_cnt[(t * r) % k] += cnt[t]
            new_cnt[r] += 1  # subarray of just this element
            cnt = new_cnt
            for x in range(k):
                result[x] += cnt[x]

        return result