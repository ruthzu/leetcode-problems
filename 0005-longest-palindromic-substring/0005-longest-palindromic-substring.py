class Solution:
    def longestPalindrome(self, s: str) -> str:
        r = ""
        for i in range(len(s)):
            l1 = self.expand(s, i, i)
            l2 = self.expand(s, i, i + 1)
            r = max(r, l1, l2, key=len)
        return r

    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
