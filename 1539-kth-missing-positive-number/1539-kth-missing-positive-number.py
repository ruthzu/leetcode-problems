class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        current = 1
        index = 0
        n = len(arr)
        while True:
            if index >= n or arr[index] != current:
                k -= 1
                if k == 0:
                    return current
            else:
                index += 1
            current += 1

