class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def parse_union(s, i):
            result = set()
            while True:
                part, i = parse_concat(s, i)
                result |= part
                if i < len(s) and s[i] == ',':
                    i += 1
                    continue
                break
            return result, i

        def parse_concat(s, i):
            sets = []
            while i < len(s) and s[i] not in ',}':
                if s[i] == '{':
                    inner, i = parse_union(s, i + 1)
                    i += 1  # skip closing brace
                    sets.append(inner)
                else:
                    sets.append({s[i]})
                    i += 1

            result = {''}
            for st in sets:
                new_result = set()
                for a in result:
                    for b in st:
                        new_result.add(a + b)
                result = new_result
            return result, i

        words, _ = parse_union(expression, 0)
        return sorted(words)