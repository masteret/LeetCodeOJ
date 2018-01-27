class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        place = {}
        count = 0
        for ind, val in enumerate(row):
            place[val] = ind
        for x in range(0, len(row), 2):
            partner = row[x]+1 if row[x]%2 == 0 else row[x]-1
            partner_pos = place[partner]
            if partner_pos-x != 1:
                row[x+1], row[partner_pos] = row[partner_pos], row[x+1]
                place[row[partner_pos]] = partner_pos
                count += 1
        return count