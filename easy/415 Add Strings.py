class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_r = num1[::-1]
        num2_r = num2[::-1]
        carry, ret, i = 0, '', 0
        while i < len(num1_r) or i < len(num2_r):
            a = 0 if i >= len(num1_r) else int(num1_r[i])
            b = 0 if i >= len(num2_r) else int(num2_r[i])
            ret += str((a+b+carry)%10)
            carry = (a + b + carry) // 10
            print(ret, carry)
            i += 1
        if carry: ret += '1'
        return ret[::-1]
if __name__ == '__main__':
    s = Solution()
    print(s.addStrings('9','99'))
