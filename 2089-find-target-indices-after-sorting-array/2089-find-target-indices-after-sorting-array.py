class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        #sorting with counting
        count=[0]*101
        for num in nums:
            count[num]+=1
        so=[]
        for i in range(1,101):
            so.extend([i]*count[i])
        result = []
        for idx, i in enumerate(so):
            if i == target:
                result.append(idx)
        return result