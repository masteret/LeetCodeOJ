class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
            bit manipulation
            start from most significant bit
            if a^1=b, then a^b=1, using this we can find the a^b result for that bit
            since we start from left to right
            more 1 bit on the left is always larger than 1 bit on the right
        """
        answer = 0
        for i in range(31,-1,-1):
            answer <<= 1
            # print '{0:b}'.format(answer),
            prefixes = {num >> i for num in nums}
            # print [(num, '{0:b}'.format(num >> i)) for num in nums], 
            # print '{0:b}'.format(answer^1),
            # print ['{0:b}'.format(answer^1^p) for p in prefixes],
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
            # print '{0:b}'.format(answer)
        return answer

a = Solution()
print a.findMaximumXOR([3, 10, 5, 25, 2, 8])