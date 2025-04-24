class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0]*101
        for num in nums:
            count[num]+=1
        so=[0]*101
        for i in range(1,101):
            so[i]=so[i-1]+count[i-1]
        result=[so[x] for x in nums]    
        return result