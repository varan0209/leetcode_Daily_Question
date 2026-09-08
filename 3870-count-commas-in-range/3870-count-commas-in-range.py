class Solution:
    def countCommas(self, n: int) -> int:
        count = 0

        for num in range(1, n + 1):
            if num >= 1000:
                count += 1

            if num >= 1000000:
                count += 1

            if num >= 1000000000:
                count += 1

        return count