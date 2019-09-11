class Solution:
    def minSteps(self, n: int) -> int:
        def factorize(num):
            factors = []
            last_factor = 2
            while num > 1:
                for i in range(last_factor, num + 1):
                    if num % i == 0:
                        factors.append(i)
                        num //= i
                        last_factor = i
                        break
            return factors

        factors = factorize(n)
        return sum(factors)
