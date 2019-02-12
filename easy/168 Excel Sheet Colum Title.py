from string import ascii_uppercase
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        list = []
        dct = dict(enumerate(ascii_uppercase, start=1))
        print(dct)
        while n:
            mod = n % 26
            n //= 26
            if mod == 0:
                mod = 26
                n -= 1
            list.append(mod)

        return ''.join([dct[i] for i in reversed(list)])

if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(26))

