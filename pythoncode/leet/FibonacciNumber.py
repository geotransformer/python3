'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).
'''


class Solution:
    def fib(self, N: int) -> int:
        '''
        # DP approach
        res = [0, 1]
        for i in range(2, N+1):
            res.append(res[i-1] + res[i-2])

        return res[N]
        '''

        # Recursion approach
        if N == 0 or N == 1:
            return N
        else:
            return self.fib(N - 1) + self.fib(N - 2)

