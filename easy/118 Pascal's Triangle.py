class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0: return result
        result.append([1])
        if numRows == 1: return result
        result.append([1,1])
        if numRows == 2: return result

        for i in range(numRows-2):
            list = [1]
            for j in range(len(result[-1])-1):
                list.append(result[-1][j] + result[-1][j+1])
            list.append(1)
            result.append(list)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))