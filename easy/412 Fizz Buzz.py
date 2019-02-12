class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            w = ''
            if i % 3 == 0: w += 'Fizz'
            if i % 5 == 0: w += 'Buzz'
            if not w : w = str(i)
            res.append(w)
        return res