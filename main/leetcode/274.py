class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        citations.sort()
        cnt = 0
        for i in range(citations[-1], 0, -1):
            for j in range(len(citations) - 1, -1, -1):
                if citations[j] >= i:
                    cnt += 1
                    if cnt == i:
                        return cnt
                else:
                    break
            if i == cnt:
                return i
            cnt = 0
        return 0

    def h_index(self, citations):
        if len(citations) == 1 and citations[0] < 1:
            return citations[0]

        citations.sort()
        for i in range(len(citations)):
            if len(citations) - i <= citations[i]:
                return len(citations) - i
        return 0