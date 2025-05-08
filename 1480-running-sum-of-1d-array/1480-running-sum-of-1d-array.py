class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        add=0
        running_sum=[]
        for i in range(len(nums)):
            add+=nums[i]
            running_sum.append(add)
        return running_sum    
