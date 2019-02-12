class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        euPrime = []
        res = 0
        is_prime = [True for i in range(n+1)]
        for i in range(2, n):
            if is_prime[i]:
                euPrime.append(i)
                res += 1
            for j in range(res):
                if i * euPrime[j] >= n:
                    break
                is_prime[i*euPrime[j]] = False
                if i % euPrime[j] == 0:
                    break
        return res