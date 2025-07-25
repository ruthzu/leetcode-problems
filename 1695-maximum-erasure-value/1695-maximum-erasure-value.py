class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=set()
        le=0
        curr_sum=0
        maxi=0
        for i in range(len(nums)):
            while nums[i] in seen:
                curr_sum-=nums[le]
                seen.remove(nums[le])
                le+=1
            seen.add(nums[i])
            curr_sum+=nums[i]
            maxi=max(maxi,curr_sum)
        return maxi 