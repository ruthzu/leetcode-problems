from collections import Counter
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        i=0
        count=Counter()
        ans=0
        for j in range(len(fruits)):
            count[fruits[j]] += 1
            while len(count)>2:
                count[fruits[i]] -=1
                if count[fruits[i]]==0:
                    del count[fruits[i]]
                i+=1
            ans= max(ans,j+1-i)  
        return ans    
