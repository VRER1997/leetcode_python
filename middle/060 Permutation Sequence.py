class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        '''
        def getP(cur,temp,dct):
            if len(ret) == k: return
            if cur == n:
                ret.append(temp)

            for i in range(1,n+1):
                if i not in dct or dct[i] == 0:
                    dct[i] = 1
                    getP(cur+1,temp+[i], dct)
                    dct[i] = 0
        ret = []
        getP(0,[],{})
        return ''.join(str(i) for i in ret[-1])
        '''
        factorial = [1] * (n+1)
        for i in range(1,n+1):
            factorial[i] = factorial[i-1]*i
        nums = [i for i in range(1,n+1)]
        k -= 1
        ret = ''
        for i in range(1,n+1):
            idx = k // factorial[n-i]
            ret += str(nums[idx])
            nums.pop(idx)
            k -= idx*factorial[n-i]
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3,3))