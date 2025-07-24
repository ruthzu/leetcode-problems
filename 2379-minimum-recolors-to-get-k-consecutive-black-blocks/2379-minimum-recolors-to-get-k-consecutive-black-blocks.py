from collections import Counter
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        left=0
        c=Counter(blocks[:k])
        ans=k-c['B']
        mini=ans
        for i in range(k,len(blocks)):
            c[blocks[i]]+=1
            left=blocks[i-k]
            c[left]-=1
            if c[left]==0:
                del c[left]
            if c['B']==k:
                return 0
            ans=k-c['B']
            mini= min(ans,mini)
        return mini

