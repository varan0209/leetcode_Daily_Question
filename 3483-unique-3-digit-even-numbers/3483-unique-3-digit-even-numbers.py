from itertools import permutations
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = []
        count = set()
        for p in permutations(digits, 3):
            if p[0] == 0:
                continue
            result.append(int("".join(map(str, p))))
        for i in range(len(result)):
            if result[i] % 2 == 0:
                count.add(result[i])
        return len(count)