Both sc and TC are logn
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        
        def rec(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            n = abs(n)
            h = n // 2

            if n % 2 == 0:
                t = rec(n//2)
                return t*t
            else:
                t = rec(n//2)
                return t*t*x

        val = rec(n)
        
        if n < 0:
            return 1/val
        else:
            return val


# We need to try the iterative soln next
        
