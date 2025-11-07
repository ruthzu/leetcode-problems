class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        neg = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        res = 0
        while a >= b:
            t, m = b, 1
            while a >= (t << 1):
                t <<= 1
                m <<= 1
            a -= t
            res += m
        return -res if neg else res
