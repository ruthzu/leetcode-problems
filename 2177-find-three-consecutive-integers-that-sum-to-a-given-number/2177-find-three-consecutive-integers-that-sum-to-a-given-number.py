class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        r=[]
        x= num//3 - 1
        if num%3!=0:
            return []
        r.extend([x,x+1,x+2])
        return r