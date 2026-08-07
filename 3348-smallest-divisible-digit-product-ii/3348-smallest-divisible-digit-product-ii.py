class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        tt = t
        a = b = c = d = 0
        while tt % 2 == 0: tt //= 2; a += 1
        while tt % 3 == 0: tt //= 3; b += 1
        while tt % 5 == 0: tt //= 5; c += 1
        while tt % 7 == 0: tt //= 7; d += 1
        if tt != 1:
            return "-1"
        target = (a, b, c, d)

        DV = {1:(0,0,0,0),2:(1,0,0,0),3:(0,1,0,0),4:(2,0,0,0),5:(0,0,1,0),
              6:(1,1,0,0),7:(0,0,0,1),8:(3,0,0,0),9:(0,2,0,0)}

        def ceil_div(x, y): return -(-x // y)

        def Mf(v):
            a, b, c, d = v
            n2 = ceil_div(a, 3)
            n3 = ceil_div(b, 2)
            if a % 3 == 1 and b % 2 == 1:
                n2n3 = n2 + n3 - 1
            else:
                n2n3 = n2 + n3
            return n2n3 + c + d

        def clamp_sub(v, w):
            return (max(0,v[0]-w[0]), max(0,v[1]-w[1]), max(0,v[2]-w[2]), max(0,v[3]-w[3]))

        def build(L, R):
            result = []
            cur = R
            for i in range(L):
                remaining_after = L - i - 1
                for dd in range(1, 10):
                    nr = clamp_sub(cur, DV[dd])
                    if Mf(nr) <= remaining_after:
                        result.append(str(dd))
                        cur = nr
                        break
            return ''.join(result)

        n = len(num)

        if '0' not in num:
            pv = (0,0,0,0)
            for ch in num:
                dv = DV[int(ch)]
                pv = (pv[0]+dv[0], pv[1]+dv[1], pv[2]+dv[2], pv[3]+dv[3])
            if all(pv[i] >= target[i] for i in range(4)):
                return num

        PE = [(0,0,0,0)] * (n + 1)
        for i in range(n):
            ch = num[i]
            dv = (0,0,0,0) if ch == '0' else DV[int(ch)]
            p0 = PE[i]
            PE[i+1] = (p0[0]+dv[0], p0[1]+dv[1], p0[2]+dv[2], p0[3]+dv[3])

        firstZero = num.find('0')
        if firstZero == -1: firstZero = n
        pmax = min(n - 1, firstZero)

        answer = None
        Mtarget = Mf(target)
        if Mtarget <= n:
            for p in range(pmax, -1, -1):
                R = clamp_sub(target, PE[p])
                low = int(num[p]) + 1
                if low > 9:
                    continue
                slots_after = n - p - 1
                chosen_d = chosen_R = None
                for dd in range(low, 10):
                    nr = clamp_sub(R, DV[dd])
                    if Mf(nr) <= slots_after:
                        chosen_d, chosen_R = dd, nr
                        break
                if chosen_d is not None:
                    suffix = build(slots_after, chosen_R)
                    answer = num[:p] + str(chosen_d) + suffix
                    break

        if answer is not None:
            return answer

        L = max(n + 1, Mtarget)
        return build(L, target)