class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        negative = []
        positive = []
        res = []

        for a in A:
            if a >= 0:
                positive.append(a ** 2)
            else:
                negative.append(a ** 2)

        p1, p2 = 0, len(negative) - 1
        for i in range(len(A)):
            if p1 == len(positive):
                res += [negative[j] for j in range(p2, -1, -1)]
                break
            if p2 == -1:
                res += positive[p1:]
                break

            if positive[p1] <= negative[p2]:
                res.append(positive[p1])
                p1 += 1
            else:
                res.append(negative[p2])
                p2 -= 1

        return res
