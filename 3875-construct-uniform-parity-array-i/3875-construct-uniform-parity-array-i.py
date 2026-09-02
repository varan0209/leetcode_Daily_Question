class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        count_odd = sum(1 for x in nums1 if x % 2 == 1)
        all_even_possible = (count_odd != 1)   # fails only if exactly one odd elem has no partner
        all_odd_possible = (count_odd >= 1)    # fails only if there's no odd elem to use as a partner
        return all_even_possible or all_odd_possible