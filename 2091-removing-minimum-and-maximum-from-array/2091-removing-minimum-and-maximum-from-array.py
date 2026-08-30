class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        i=nums.index(min(nums))
        j=nums.index(max(nums))
        n=len(nums)
        if i>j:
            temp=i
            i=j
            j=temp
        front=j+1
        back=n-i
        both=(i+1)+(n-j)
        return min(front,back,both)