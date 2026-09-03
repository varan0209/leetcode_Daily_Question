class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = inf
        even = inf
        
        for n in nums1:
            if n % 2:
                odd = min(odd, n)
            else:
                even = min(even, n)

        if odd == inf or even == inf:
            return True

        return odd < even