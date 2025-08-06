from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tcount = Counter(t)    
        scount = {}               

        i, j = 0, len(tcount)  
        res = [-1, -1]
        res_len = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            scount[char] = scount.get(char, 0) + 1

            if char in tcount and scount[char] == tcount[char]:
                i += 1

            while i == j:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                scount[s[left]] -= 1
                if s[left] in tcount and scount[s[left]] < tcount[s[left]]:
                    i -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
