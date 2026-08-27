from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        # Determine the longest prefix of target that can be exactly matched
        # using available letters in s.
        cnt_copy = cnt.copy()
        max_prefix = 0
        for i in range(n):
            c = target[i]
            if cnt_copy[c] > 0:
                cnt_copy[c] -= 1
                max_prefix = i + 1
            else:
                break
        
        # counts holds the remaining letter counts after matching target[0:i]
        counts = cnt_copy.copy()
        
        for i in range(max_prefix, -1, -1):
            if i < n:
                # Find the smallest available letter strictly greater than target[i]
                best_char = None
                for ch in sorted(k for k, v in counts.items() if v > 0):
                    if ch > target[i]:
                        best_char = ch
                        break
                if best_char:
                    counts[best_char] -= 1
                    remaining = []
                    for ch2 in sorted(k for k, v in counts.items() if v > 0):
                        remaining.extend([ch2] * counts[ch2])
                    return target[:i] + best_char + ''.join(remaining)
            
            # Reduce prefix length by 1: add back target[i-1] to counts
            if i > 0:
                counts[target[i - 1]] = counts.get(target[i - 1], 0) + 1
        
        return ""