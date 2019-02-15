class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12 or len(s) < 4:
            return []

        def isVaild(ip):
            """
            :param ip: str:
            :return: Bool
            """
            if ip.count('.') != 3:
                return False
            lst = ip.split('.')
            for num in lst:
                if not num or int(num) > 255 or (len(num) > 1 and num[0] == '0'):
                    return False
            return True

        self.ret = []

        def dfs(tem, idx, cnt):
            if cnt == 3:
                #print(tem)
                if isVaild(tem):
                    self.ret.append(tem)
                return
            if idx == len(tem):
                return
            dfs(tem, idx + 1, cnt)
            dfs(tem[:idx] + '.' + tem[idx:], idx + 1, cnt + 1)

        dfs(s, 0, 0)
        return self.ret

if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))