class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        lst = []
        for i in range(0,5):
            if i > num: break
            l = self.read(i,0)
            r = self.read(num-i,1)
            for char_x in l:
                for char_y in r:
                    lst.append(char_x+':'+char_y)
        return lst

    def read(self, num, type):
        ret = []
        if type == 0: r = 12
        else: r = 60
        for i in range(r):
            if self.readCountOne(i) == num:
                t = str(i)
                if 0 <= i < 10 and type == 1 :
                    t = '0' + t
                ret.append(t)
        return ret

    def readCountOne(self, num):
        cnt = 0
        while num :
            cnt += num % 2
            num //= 2
        return cnt

if __name__ == '__main__':
    s = Solution()
    print(s.readBinaryWatch(10))