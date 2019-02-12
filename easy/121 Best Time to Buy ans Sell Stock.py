class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        maxs = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                maxs += prices[i+1] - prices[i]
        return maxs