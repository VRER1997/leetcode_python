class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        '''
        The main problem is we need to convert binary code B to Gray code G.
        For the i th bit of binary code:
        if i==0: G[i]=B[i]
        else: G[i] = B[i] XOR B[i-1]
        
        The above part can be simply expressed by G = B^(B>>1).
        '''
        return [(i>>1)^i for i in range(pow(2,n))]