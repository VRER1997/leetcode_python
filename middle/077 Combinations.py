class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(2**n):
            if bin(i).count('1') == k:
                indexs = []
                for index, char in enumerate(str(bin(i))[::-1]):
                    if char == '1': indexs.append(index+1)
                ret.append(indexs)
        return ret

if __name__ == '__main__':
    s = Solution()
    s.combine(4,2)