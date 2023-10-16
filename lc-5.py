isPalind = [[0 for i in range(1001)] for j in range(1001)]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # init a 2d array
        maxlen = len(s)
        # do not use this, each row are just copies

        # init answer
        sublen_max = 0
        start_max = None
        end_max = None

        # iterate substring length from 1 to maxlen
        for sublen in range(1, maxlen + 1):
            for start in range(0, maxlen):
                end = start + sublen - 1
                if end >= maxlen:
                    break

                if sublen == 1:
                    isPalind[start][end] = True
                elif sublen == 2:
                    isPalind[start][end] = (s[start] == s[end])
                else:
                    isPalind[start][end] = isPalind[start + 1][end - 1] and (s[start] == s[end])
                
                if isPalind[start][end]:
                    if sublen > sublen_max:
                        sublen_max = sublen
                        start_max = start
                        end_max = end

        # print(isPalind)
        return s[start_max: end_max + 1]


sol = Solution()
ret = sol.longestPalindrome("babadee")

print(ret)


