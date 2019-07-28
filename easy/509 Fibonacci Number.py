class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        lst = [0, 1]
        for i in range(N-1):
            lst.append(lst[-1] + lst[-2])
        return lst[-1]