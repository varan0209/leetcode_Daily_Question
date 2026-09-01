class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        sr = sc = -1
        litter_idx = {}
        for i in range(m):
            for j in range(n):
                c = classroom[i][j]
                if c == 'S':
                    sr, sc = i, j
                elif c == 'L':
                    litter_idx[(i, j)] = len(litter_idx)

        L = len(litter_idx)
        target = (1 << L) - 1
        if L == 0:
            return 0

        # best[r][c][mask] = max energy achieved so far at that (r,c,mask)
        best = [[dict() for _ in range(n)] for _ in range(m)]
        best[sr][sc][0] = energy

        q = deque()
        q.append((sr, sc, 0, energy, 0))  # row, col, mask, energy, moves

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, mask, e, moves = q.popleft()

            # skip stale entries superseded by a later, better-energy record
            if best[r][c].get(mask, -1) != e:
                continue
            if e <= 0:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                cell = classroom[nr][nc]
                if cell == 'X':
                    continue

                ne = e - 1
                if cell == 'R':
                    ne = energy

                nmask = mask
                if (nr, nc) in litter_idx:
                    nmask = mask | (1 << litter_idx[(nr, nc)])

                if nmask == target:
                    return moves + 1

                if ne > best[nr][nc].get(nmask, -1):
                    best[nr][nc][nmask] = ne
                    q.append((nr, nc, nmask, ne, moves + 1))

        return -1