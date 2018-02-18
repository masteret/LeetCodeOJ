class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        markers = [[1, ""]]
        cur_str = ""
        cur_num = ""
        for x in s:
            if x.isdigit():
                cur_num += x
            elif x == "[":
                markers.append([int(cur_num), ""])
                cur_num = ""
            elif x == "]":
                times, text = markers.pop(-1)
                text = text*times
                markers[-1][1] += text
            else:
                markers[-1][1] += x
        return markers[0][1]

a = Solution()
print a.decodeString("3[a]2[bc]")