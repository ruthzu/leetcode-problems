class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=[]
        temp=int("".join(map(str,digits)))+1
        print(temp)
        for i in str(temp):
            ans.append(int(i))
        return ans