#python  Android: Java  web: Java PHP Javascript
class Solution:
    # rever
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        str_x = str(x)
        res = ''
        if str_x[0] == '-':
            res = '-'
        res += str_x[len(str_x)-1::-1].lstrip('0').rstrip('-')
        res = int(res)
        print(res)
        if -2 ** 31 < res < 2 ** 31 - 1:
            return res
        return 0


if __name__ == '__main__':
    s = Solution()
    s.reverse(0)