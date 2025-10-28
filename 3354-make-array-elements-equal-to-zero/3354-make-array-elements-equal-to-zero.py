class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0

        def sim(i, d):
            arr = nums.copy()
            cur = i
            dir = d
            while 0 <= cur < n:
                if arr[cur] == 0:
                    cur += dir
                else:
                    arr[cur] -= 1
                    dir = -dir
                    cur += dir
            return all(x == 0 for x in arr)

        for i in range(n):
            if nums[i] == 0:
                if sim(i, 1):
                    res += 1
                if sim(i, -1):
                    res += 1
        return res
