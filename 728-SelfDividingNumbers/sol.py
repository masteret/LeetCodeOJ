class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left, right+1):
            if "0" in str(num):
                continue
            for digit in str(num):
                if digit == "0":
                    break
                if num % int(digit) != 0:
                    break
            else:
                result.append(num)
        return result