class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for x in arr1:
            count[x] = count.get(x, 0) + 1
        result = []
        for x in arr2:
            if x in count:
                result.extend([x] * count[x])
                del count[x]  
        for x in sorted(count.keys()):
            result.extend([x] * count[x])
        return result
