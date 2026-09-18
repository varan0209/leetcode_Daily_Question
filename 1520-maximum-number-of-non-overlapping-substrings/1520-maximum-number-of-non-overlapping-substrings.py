class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []
        for i in range(n):
            ch = s[i]
            if first[ch] != i:
                continue
            end = last[ch]
            j = i
            valid = True
            while j <= end:
                c2 = s[j]
                if first[c2] < i:
                    valid = False
                    break
                if last[c2] > end:
                    end = last[c2]
                j += 1
            if valid:
                intervals.append((i, end))

        intervals.sort(key=lambda x: x[1])
        res = []
        last_end = -1
        for st, en in intervals:
            if st > last_end:
                res.append(s[st:en + 1])
                last_end = en
        return res