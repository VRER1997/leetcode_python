class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        result.append([1])
        if rowIndex == 0: return result[-1]
        result.append([1, 1])
        if rowIndex == 1: return result[-1]

        for i in range(rowIndex - 1):
            list = [1]
            for j in range(len(result[-1]) - 1):
                list.append(result[-1][j] + result[-1][j + 1])
            list.append(1)
            result.append(list)
        return result[-1]