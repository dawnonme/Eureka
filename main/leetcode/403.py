'''  Frog Jump '''


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        ''' Dynamic Programming '''
        from collections import defaultdict

        if not stones:
            return True

        dp = defaultdict(set)
        dp[1] = set([1])  # first step must be 1

        stones_set = set(stones)
        for i, v in enumerate(stones):
            if v == 0:
                continue
            for prev_k in dp[v]:
                for next_k in [prev_k - 1, prev_k, prev_k + 1]:
                    if v + next_k in stones_set and next_k != 0:
                        dp[v + next_k].add(next_k)
        return len(dp[stones[-1]]) > 0

    def can_cross(self, stones: List[int]) -> bool:
        ''' DFS '''
        jump_stack = [(0, 0)]
        stones_set = set(stones)
        visited = set()

        while jump_stack:
            pos, step = jump_stack.pop()
            if pos == stones[-1]:
                return True
            visited.add((pos, step))
            for next_step in range(step - 1, step + 2):
                next_pos = pos + next_step
                if next_pos in stones_set and (next_pos, next_step) not in visited:
                    jump_stack.append((next_pos, next_step))

        return False
