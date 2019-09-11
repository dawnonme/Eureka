class Solution:
    def soupServings(self, N: int) -> float:
        if N >= 4000:
            return 1

        self.ans, self.dp = 0, {}
        self.operations = [(100, 0), (75, 25), (50, 50), (25, 75)]
        return self.__soupServings(N, N)

    def __soupServings(self, A, B):
        if A <= 0 and B <= 0:
            return 0.5
        if A <= 0:
            return 1.0
        if B <= 0:
            return 0.0

        if (A, B) not in self.dp:
            self.dp[(A, B)] = 0.25 * sum([
                self.__soupServings(A - self.operations[op][0],
                                    B - self.operations[op][1])
                for op in range(4)
            ])

        return self.dp[(A, B)]
