class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)

        # Calculate free copies earned by buying each item type
        bonus = [0] * n

        for i in range(n):
            factor_i = items[i][0]

            for j in range(n):
                if i != j and items[j][0] % factor_i == 0:
                    bonus[i] += 1

        # dp[b] = maximum total items using at most budget b
        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            free = bonus[i]

            prev = dp[:]
            cur = dp[:]

            for b in range(price, budget + 1):

                # Buy the first copy of this item type
                cur[b] = max(
                    cur[b],
                    prev[b - price] + free + 1
                )

                # Buy additional copies of this same type
                cur[b] = max(
                    cur[b],
                    cur[b - price] + 1
                )

            dp = cur

        return max(dp)