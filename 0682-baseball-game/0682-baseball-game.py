class Solution:
    def calPoints(self, operations: List[str]) -> list:
        arr= []
        for i in operations:
            if i == 'C':
                if arr:
                    arr.pop()
            elif i == 'D':
                if arr:
                    arr.append(2 * arr[-1])
            elif i == '+':
                if len(arr) >= 2:
                    arr.append(arr[-1] + arr[-2])
            else:
                arr.append(int(i))
        return sum(arr)  