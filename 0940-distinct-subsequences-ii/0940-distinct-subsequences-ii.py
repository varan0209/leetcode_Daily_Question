class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        end = {}      # end[c] = distinct subsequences ending in character c
        total = 0      # running total of all distinct non-empty subsequences

        for ch in s:
            prev = end.get(ch, 0)
            new_count = (total + 1) % MOD
            total = (total - prev + new_count) % MOD
            end[ch] = new_count

        return total % MOD