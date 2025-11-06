class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))[::-1]
        r = int(s)
        if r > 2**31 - 1:
            return 0
        return r if x >= 0 else -r
