class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            neg = False
        else:
            neg = True
            x = -x
        sx = str(x)
        sxr = sx[::-1]
        xr = int(sxr) if not neg else -int(sxr)
        if xr > 2**31 - 1 or xr < -2**31:
            xr = 0
        return xr
