__author__ = 'ET'
import math

class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        return math.factorial(2*n)/(math.factorial(n+1)*math.factorial(n))

if __name__ == "__main__":
    puppy = Solution()
    print puppy.numTrees(3)
    print puppy.numTrees(1)
    print puppy.numTrees(5)
    print puppy.numTrees(20)
    print puppy.numTrees(100)
    print puppy.numTrees(1000)