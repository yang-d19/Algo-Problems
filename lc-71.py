class Solution(object):
    def simplifyPath(self, path: str):
        """
        :type path: str
        :rtype: str
        """
        ops = path.split('/')
        
        dir_stack = []
        for op in ops:
            if op == '':
                continue
            elif op == '.':
                continue
            elif op == '..':
                if len(dir_stack) > 0:
                    dir_stack.pop()
            else:
                dir_stack.append(op)
        
        canonical_path = ''
        for d in dir_stack:
            canonical_path += '/' + d
        if len(dir_stack) == 0:
            canonical_path += '/'
        
        return canonical_path

sol = Solution()
path = "/home/"
res = sol.simplifyPath(path)

print(res)