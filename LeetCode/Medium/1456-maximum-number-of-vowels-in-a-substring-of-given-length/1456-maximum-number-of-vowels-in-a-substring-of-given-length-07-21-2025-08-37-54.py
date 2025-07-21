class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vow=set('aeiou')
        count =0
        for i in range(k):
            if s[i] in vow:
                count+=1
        maxi=count
        for i in range(k,len(s)):
            if s[i] in vow:
                count+=1
            if s[i-k] in vow:
                count-=1
            maxi=max(maxi,count)
        return maxi    
