class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # sort indices by their value
        indexed = sorted(range(n), key=lambda i: nums[i])
        
        ans = [0] * n
        i = 0
        while i < n:
            j = i
            # extend the group while consecutive sorted values stay within limit
            while j + 1 < n and nums[indexed[j + 1]] - nums[indexed[j]] <= limit:
                j += 1
            
            # collect original indices and values for this group
            group_positions = sorted(indexed[i:j + 1])       # original positions, ascending
            group_values = [nums[k] for k in indexed[i:j + 1]]  # values, already ascending
            
            # assign smallest value to smallest position, etc.
            for pos, val in zip(group_positions, group_values):
                ans[pos] = val
            
            i = j + 1
        
        return ans