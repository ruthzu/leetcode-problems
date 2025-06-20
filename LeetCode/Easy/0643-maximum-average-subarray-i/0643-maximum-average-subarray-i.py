class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        numss=nums[:k]
        add=sum(numss)
        avg=add/k
        for i in range(k,len(nums)):
            add-=nums[i-k]
            add+=nums[i]
            avg=max(avg, add/k)
        return avg    

            