class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) ^ (divisor < 0)
        if negative:
            dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            dividend -= divisor
            res += 1
        return -res if negative else res