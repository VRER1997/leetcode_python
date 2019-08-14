class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '' or b == '':
            return a + b
        elif a[-1] == '0' and b[-1] =='0':
            return self.addBinary(a[:-1],b[:-1]) + '0'
        elif a[-1] == '1' and b[-1] == '1':
            return self.addBinary(a[:-1],self.addBinary(b[:-1], '1')) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'



if __name__ == '__main__':
    s = Solution();
    print(s.addBinary('1010', '1011'))