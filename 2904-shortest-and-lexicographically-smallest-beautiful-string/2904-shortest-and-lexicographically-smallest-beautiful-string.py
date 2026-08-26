class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        min_len = float('inf')
        best = ""
        
        left = 0
        ones = 0
        
        for right in range(n):
            if s[right] == '1':
                ones += 1
            
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1
            
            if ones == k:
                # shrink from left as much as possible while keeping ones == k
                while s[left] == '0':
                    left += 1
                
                length = right - left + 1
                if length < min_len:
                    min_len = length
                    best = s[left:right+1]
                elif length == min_len:
                    candidate = s[left:right+1]
                    if candidate < best:
                        best = candidate
        
        return best