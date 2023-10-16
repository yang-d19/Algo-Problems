class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        last_say = self.countAndSay(n - 1)
        this_say = ""
        same_cnt = 1

        for i in range(1, len(last_say)):
            if last_say[i] == last_say[i - 1]:
                same_cnt += 1
            else:
                this_say += str(same_cnt) + last_say[i - 1]
                same_cnt = 1

        this_say += str(same_cnt) + last_say[len(last_say) - 1]

        return this_say


sol = Solution()

ret = sol.countAndSay(7)

print(ret)