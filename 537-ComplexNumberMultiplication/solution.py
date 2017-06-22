class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        val1, val2 = a.split("+")
        val3, val4 = b.split("+")
        val1 = int(val1)
        val2 = int(val2[:-1])
        val3 = int(val3)
        val4 = int(val4[:-1])
        val5 = val1*val3 - val2*val4
        val6 = val2*val3 + val1*val4
        return str(val5) + "+" + str(val6) + "i"

a = Solution()
print a.complexNumberMultiply("1+-1i", "1+-1i")
print a.complexNumberMultiply("1+1i", "1+1i")