class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        max_int = 0x7fffffff
        min_int = 0x80000000
        mask = 0xffffffff
        if b == 0:
            # if larger than 32 bit max int, make it into negative
            return a if a <= max_int else ~(a ^ mask)
        # calculate all the one bit
        value = (a ^ b) & mask
        # if there is a shift, shift will be > 0
        shift = ((a & b) << 1) & mask
        return self.getSum(value, shift)