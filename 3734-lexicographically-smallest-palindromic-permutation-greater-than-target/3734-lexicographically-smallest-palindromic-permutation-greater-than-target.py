class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        cnt = Counter(s)

        # A palindrome can have at most one odd-frequency character
        odd = [c for c in cnt if cnt[c] % 2]

        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""

        # Count characters for the left half
        half_count = [0] * 26

        for i in range(26):
            ch = chr(97 + i)
            half_count[i] = cnt[ch] // 2

        m = len(s) // 2

        def build(left):
            left = ''.join(left)
            return left + middle + left[::-1]

        # Try to match target's first half
        left = []
        remaining = half_count[:]
        mismatch = -1

        for i in range(m):
            t = ord(target[i]) - 97

            if remaining[t] > 0:
                left.append(chr(97 + t))
                remaining[t] -= 1
            else:
                mismatch = i
                break

        # Case 1: We matched the entire first half
        if mismatch == -1:
            candidate = build(left)

            if candidate > target:
                return candidate

            # Otherwise, we need to increase the half.
            start = m - 1

        # Case 2: We couldn't match target at position mismatch
        else:
            start = mismatch

        # Find the rightmost position we can increase
        for i in range(start, -1, -1):

            # Characters used before position i
            remaining = half_count[:]

            for j in range(i):
                remaining[ord(left[j]) - 97] -= 1

            # We need a character greater than target[i]
            target_char = ord(target[i]) - 97

            for c in range(target_char + 1, 26):
                if remaining[c] > 0:

                    new_left = left[:i] + [chr(97 + c)]
                    remaining[c] -= 1

                    # Fill the rest with the smallest characters
                    for x in range(26):
                        new_left.extend(
                            [chr(97 + x)] * remaining[x]
                        )

                    return build(new_left)

        return ""