from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counts = Counter(digits)
        found = set()

        for hundreds in range(1, 10):
            if counts[hundreds] == 0:
                continue
            for tens in range(0, 10):
                if counts[tens] == 0 or (tens == hundreds and counts[tens] < 2):
                    continue
                for units in range(0, 10, 2):
                    need = Counter([hundreds, tens, units])
                    if all(counts[d] >= need[d] for d in need):
                        found.add(hundreds * 100 + tens * 10 + units)

        return len(found)