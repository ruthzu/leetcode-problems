class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp={}
        for i in range(len(names)):
            temp[heights[i]]=names[i]
        ans=[]
        result=sorted(heights ,reverse=True)
        for i in result:
            ans.append(temp[i])
        return ans    
