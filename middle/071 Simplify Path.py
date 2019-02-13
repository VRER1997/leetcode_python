class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split('/')
        for part in parts:
            if part != '' and part !='.':
                if part == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(part)
        if not stack:
            return "/"
        else:
            return '/'+'/'.join(stack)

if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/home/stdy"))
