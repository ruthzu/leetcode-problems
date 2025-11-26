class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        
        c = 0
        m = 0
        for i in range(n):
            ans[i] += m
            if boxes[i] == '1':
                c += 1
            m += c
        
        c = 0
        m = 0
        for i in range(n - 1, -1, -1):
            ans[i] += m
            if boxes[i] == '1':
                c += 1
            m += c
        
        return ans
