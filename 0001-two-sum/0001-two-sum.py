class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        paired = list(enumerate(nums))
        paired.sort(key=lambda x: x[1])
        while left<right:
            cursum=paired[left][1]+paired[right][1]
            if cursum==target:
               return (paired[left][0],paired[right][0])
            elif cursum<target:
                left+=1
            else:
                right-=1
        return[]   