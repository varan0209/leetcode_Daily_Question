class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Pascal's triangle mod p
        C = [[1] * (i + 1) for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        result = 1
        stack = [nums]
        while stack:
            arr = stack.pop()
            if len(arr) <= 2:
                continue  # 0/1 element: 1 way; 2 elements: root fixed, 1 way
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            result = result * C[len(arr) - 1][len(left)] % MOD
            stack.append(left)
            stack.append(right)

        return (result - 1) % MOD