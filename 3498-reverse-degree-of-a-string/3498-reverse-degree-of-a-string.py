class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        total = 123 * n * (n + 1) // 2
        
        sub = 0
        idx = 1
        _ord = ord 
        
        for ch in s:
            sub += _ord(ch) * idx
            idx += 1
            
        return total - sub