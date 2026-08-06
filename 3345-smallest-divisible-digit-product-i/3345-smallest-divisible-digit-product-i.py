class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            p =1
            temp = n

            while temp > 0:
                digit = temp % 10
                p = p * digit
                temp = temp // 10
            
            if p % t == 0:
                return n
            n += 1    