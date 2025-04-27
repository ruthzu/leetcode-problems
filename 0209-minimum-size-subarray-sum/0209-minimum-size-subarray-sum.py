class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n= len(nums)
        left=0
        add=0
        result=float('inf')
        for i in range(n):
            add+=nums[i]
            while add>=target:
                result=min(result,i-left+1)
                add-=nums[left]
                left+=1
        if result != float('inf'):
            return result
        else:
            return 0            
