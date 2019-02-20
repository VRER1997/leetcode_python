class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank, start = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank, start = 0, i+1
        return -1 if sum(gas) < sum(cost) else start


        """
        n = len(gas)
        def check(i):
            remain, cnt = gas[i], 0
            while cnt <= n:
                remain -= cost[i]
                if remain < 0: return False
                i = (i+1) % n
                cnt += 1
                remain += gas[i]
            return True

        for i in range(n):
            if check(i):
                return i
        return -1
        """