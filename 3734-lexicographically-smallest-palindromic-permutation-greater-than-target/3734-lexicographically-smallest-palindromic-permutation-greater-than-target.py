from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        odd_chars = [c for c, v in cnt.items() if v % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        if len(odd_chars) == 1 and n % 2 == 0:
            return ""
        if len(odd_chars) == 0 and n % 2 == 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_len = n // 2
        half_counts = {c: v // 2 for c, v in cnt.items()}
        
        # Try to match target's first half exactly (greedy character-by-character)
        counts_copy = half_counts.copy()
        max_prefix = 0
        for i in range(half_len):
            c = target[i]
            if counts_copy.get(c, 0) > 0:
                counts_copy[c] -= 1
                max_prefix = i + 1
            else:
                break
        
        # Case A: H == target[:half_len] exactly (uses ALL of half_counts, since
        # a full greedy match over half_len positions must consume everything)
        if max_prefix == half_len:
            H = target[:half_len]
            candidate_A = H + mid_char + H[::-1]
            if candidate_A > target:
                return candidate_A
        
        # Case B: find the smallest H strictly greater than target[:half_len]
        counts = counts_copy.copy()
        for i in range(max_prefix, -1, -1):
            if i < half_len:
                best_char = None
                for ch in sorted(k for k, v in counts.items() if v > 0):
                    if ch > target[i]:
                        best_char = ch
                        break
                if best_char:
                    new_counts = counts.copy()
                    new_counts[best_char] -= 1
                    left = list(target[:i]) + [best_char]
                    remaining = []
                    for ch2 in sorted(k for k, v in new_counts.items() if v > 0):
                        remaining.extend([ch2] * new_counts[ch2])
                    left.extend(remaining)
                    H = ''.join(left)
                    candidate = H + mid_char + H[::-1]
                    if candidate > target:
                        return candidate
            
            if i > 0:
                counts[target[i - 1]] = counts.get(target[i - 1], 0) + 1
        
        return ""