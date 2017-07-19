class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        unique = set(candies)
        if len(candies)/2 >= len(unique):
            return len(unique)
        else:
            return len(candies)/2