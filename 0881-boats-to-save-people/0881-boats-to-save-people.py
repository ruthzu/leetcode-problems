class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i, add, j = 0, 0, len(people)-1
        pep=sorted(people)
        n=len(pep)
        while i<=j:  
            if pep[i] + pep[j]<=limit:
                i+=1
            j-=1 
            add+=1  
        return add     