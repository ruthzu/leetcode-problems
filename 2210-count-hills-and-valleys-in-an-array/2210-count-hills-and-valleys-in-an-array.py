class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        a = [nums[0]]
        for x in nums[1:]:
            if x != a[-1]:
                a.append(x)
        
        c = 0
        for i in range(1, len(a)-1):
            if a[i] > a[i-1] and a[i] > a[i+1]:
                c += 1
            elif a[i] < a[i-1] and a[i] < a[i+1]:
                c += 1
        
        return c
