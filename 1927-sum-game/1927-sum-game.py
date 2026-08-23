class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum1, cnt1 = 0, 0
        for i in range(half):
            if num[i] == '?':
                cnt1 += 1
            else:
                sum1 += int(num[i])
        
        sum2, cnt2 = 0, 0
        for i in range(half, n):
            if num[i] == '?':
                cnt2 += 1
            else:
                sum2 += int(num[i])
        
        total_q = cnt1 + cnt2
        
        # Odd total '?' count: Alice always wins
        if total_q % 2 == 1:
            return True
        
        diff = sum1 - sum2
        forced_diff = diff + 9 * (cnt1 - cnt2) // 2
        
        return forced_diff != 0