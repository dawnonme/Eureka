class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        ret = [m[:] for m in M]

        for i in range(len(M)):
            for j in range(len(M[0])):
                val, num_ele = 0, 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        new_i, new_j = i + di, j + dj
                        if (
                            new_i >= 0
                            and new_i < len(M)
                            and new_j >= 0
                            and new_j < len(M[0])
                        ):
                            val += M[new_i][new_j]
                            num_ele += 1
                ret[i][j] = val // num_ele

        return ret
