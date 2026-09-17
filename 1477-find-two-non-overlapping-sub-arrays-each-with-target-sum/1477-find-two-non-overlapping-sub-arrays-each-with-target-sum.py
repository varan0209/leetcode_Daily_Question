class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        best = [INF] * n  # best[i] = shortest valid subarray ending at index <= i

        ans = INF
        left = 0
        curr_sum = 0

        for right in range(n):
            curr_sum += arr[right]
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, best[left - 1] + length)
                best[right] = min(best[right - 1] if right > 0 else INF, length)
            else:
                best[right] = best[right - 1] if right > 0 else INF

        return ans if ans != INF else -1