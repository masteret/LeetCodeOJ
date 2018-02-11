class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        rev = [int(x) for x in str(N)[::-1]]
        ind = -1
        for x in range(1, len(rev)):
            if rev[x] > rev[x-1] or (ind != -1 and rev[ind] == rev[x]):
                ind = x

        if ind == -1:
            return N

        for x in range(ind):
            rev[x] = 9

        rev[ind] -= 1
        return int(''.join([str(x) for x in rev[::-1]]))