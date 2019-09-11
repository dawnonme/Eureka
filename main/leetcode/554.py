class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import Counter

        counter = Counter()
        max_reach = 0

        for i in range(len(wall)):
            length = 0
            for j in range(len(wall[i]) - 1):
                length += wall[i][j]
                counter[length] += 1
                # max_reach = max(max_reach, counter[length])
        max_reach = max([v for k, v in counter.items()])
        return len(wall) - max_reach