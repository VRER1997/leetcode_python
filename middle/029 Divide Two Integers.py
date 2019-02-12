class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #首先这一句就很python，postive 为true是符号相同
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        #检查dividend是否大于divisor
        #如果还小于则进行小精度的逼近dividend
        while dividend >= divisor:
            temp, i = divisor, 1
            #增大逼近dividend的步伐
            #i不断增加， temp不断减少
            while dividend >= temp:
                #经过上一句的判断，所以dividend还大于0
                dividend -= temp
                #商要加对应的i
                res += i
                #倍数相应的要增加
                i = i<<1
                #目前的值也要不断的增加
                temp = temp<<1
        #判定正负号
        if not positive:
            res = -res
        return min(max(-2147483648,res), 2147483647)