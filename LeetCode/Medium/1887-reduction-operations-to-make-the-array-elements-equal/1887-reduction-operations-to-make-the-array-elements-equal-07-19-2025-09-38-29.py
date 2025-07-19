class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        j=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                j+=1
            k+=j
        return k       