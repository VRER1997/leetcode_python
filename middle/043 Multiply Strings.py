class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # def str2int(num):
        #     res = 0
        #     for i in range(len(num)-1, 0, -1):
        #         res += int(num[i]) * pow(10, len(num)-1-i)
        #     return res
        if num1 == '0' or num2 == '0': return '0'
        dct = {}
        for i in range(10):
            dct[str(i)] = i
        num1_r, num2_r = num1[::-1], num2[::-1]

        temp = [0 for i in range(len(num1+num2))]
        ret = [0 for i in range(len(num1 + num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp[i+j] += dct[num1_r[i]] * dct[num2_r[j]]
            print(temp)

        for i in range(len(temp)):
            ret[i] = temp[i] % 10
            if i < len(temp)-1:
                temp[i+1] += temp[i]//10
        return ''.join(str(i) for i in ret[::-1]).lstrip('0')

if __name__ == '__main__':
    s = Solution()
    print(s.multiply('123','456'))