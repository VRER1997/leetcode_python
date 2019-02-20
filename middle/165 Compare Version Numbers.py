class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        n1, n2, flag = len(v1), len(v2), False
        if n1 > n2: v2 += [0]*(n1-n2)
        elif n1 < n2: v1 += [0]*(n2-n1)
        else:flag = True

        i = 0
        while i < len(v1) and i < len(v2):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            i += 1
        return 0

if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion("01", "1.0"))