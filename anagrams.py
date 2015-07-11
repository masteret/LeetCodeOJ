__author__ = 'ET'

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        if len(strs) < 2:
            return []
        str_dict = {}
        for word in strs:
            parsed = str(sorted(word))
            if str_dict.get(parsed) is None:
                str_dict.update({parsed:[word]})
            else:
                str_dict.get(parsed).append(word)

        result_list = []
        for item in str_dict.values():
            if len(item) > 1:
                result_list.extend(item)

        return result_list


if __name__ == "__main__":
    puppy = Solution()
    print puppy.anagrams(["iceman", "manice"])
    print puppy.anagrams(["iceman"])
    print puppy.anagrams([""])
    print puppy.anagrams([])
    print puppy.anagrams(["","b"])
    print puppy.anagrams(["tea","and","ate","eat","dan"])