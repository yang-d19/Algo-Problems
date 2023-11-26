"""
Group Anagrams
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        id_orig_dict = {}
        
        for idx in range(len(strs)):
            sort_chs = sorted(strs[idx])
            id_str = ""
            for ch in sort_chs:
                id_str += ch
            if id_str not in id_orig_dict:
                id_orig_dict[id_str] = [strs[idx]]
            else:
                id_orig_dict[id_str].append(strs[idx])
        
        ans = []

        for key, value in id_orig_dict.items():
            ans.append(value)
        
        return ans

sol = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

result = sol.groupAnagrams(strs)

print(result)
