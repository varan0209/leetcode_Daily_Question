class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1) % 2:
            return True

        f = True
        for num in nums1:
            if num % 2:
                f = False
                break
        
        return f
