class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            mid = 0
            if nums[i]== target:
                return i
            elif nums[i]== target - 1:
                return i+1    
            elif nums[i]== target + 1:
                return i-1 
            elif nums[0]>= target:
                return 0  