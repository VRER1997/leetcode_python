class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ret = 1
        for i in range(1000):
            ret = (ret+num/ret)//2
            if ret ** 2 == num:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    s.isPerfectSquare(10000)