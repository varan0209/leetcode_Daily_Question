class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # suf[i] = number of trailing chars of word2 that can be matched
        # exactly (as a subsequence) using word1[i:]
        suf = [0] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = m - 1 - j
        
        result = []
        j = 0
        used_skip = False
        
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                result.append(i)
                j += 1
            elif not used_skip and suf[i + 1] >= m - j - 1:
                result.append(i)
                used_skip = True
                j += 1
        
        return result if j == m else []