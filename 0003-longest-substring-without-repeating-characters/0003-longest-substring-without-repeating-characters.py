class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=set()
        left=0
        max_sub=0
        for i in range(len(s)):
            while s[i] in sub:
                sub.remove(s[left])
                left+=1
            sub.add(s[i])
            max_sub=max(max_sub,len(sub))
        return max_sub           