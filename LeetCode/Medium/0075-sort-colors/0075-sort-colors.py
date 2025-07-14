class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=nums.count(0)
        one=nums.count(1)
        two=nums.count(2)
        nums[0:zero]=[0]*zero
        nums[zero:zero+one]=[1]*one
        nums[zero+one:len(nums)]=[2]*two