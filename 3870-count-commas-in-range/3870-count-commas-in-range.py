class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        for x in range(1, n + 1):
            digits = len(str(x))
            total += (digits - 1) // 3
        return total