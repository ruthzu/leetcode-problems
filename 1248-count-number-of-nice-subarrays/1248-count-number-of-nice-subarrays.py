class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMostK(k):
            count = 0
            i = 0
            ans = 0
            for j in range(len(nums)):
                if nums[j] % 2 != 0:
                    count += 1
                while count > k:
                    if nums[i] % 2 != 0:
                        count -= 1
                    i += 1
                ans += j - i + 1
            return ans
        return atMostK(k) - atMostK(k - 1)
