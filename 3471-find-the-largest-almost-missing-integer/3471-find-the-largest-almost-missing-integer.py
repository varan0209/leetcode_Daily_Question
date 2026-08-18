class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # k가 전체 길이와 같으면 무조건 최댓값
        if k == len(nums):
            return max(nums)

        # k == 1이면 1번만 나온 숫자 중 최댓값
        if k == 1:
            arr = [x for x in nums if nums.count(x) == 1]
        
        # 위에 해당되지 않으면 nums[0], nums[-1]만 후보임
        else:
            arr = [x for x in (nums[0], nums[-1]) if nums.count(x) == 1]
        
        # arr 없으면 -1
        return max(arr) if arr else -1