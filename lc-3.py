class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        start = 0
        end = start

        max_len = 0

        while end < len(s):
            val = d.get(s[end])

            if val == None:
                d[s[end]] = 1
                end += 1
                
            else:
                while s[start] != s[end]:
                    del d[s[start]]
                    start += 1
                start += 1
                end += 1
            
            if end - start > max_len:
                max_len = end - start
        
        return max_len
                
s = "tmmzuxt"

sol = Solution()
ret = sol.lengthOfLongestSubstring(s)

print(ret)
