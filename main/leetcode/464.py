class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        choices = list(range(1, maxChoosableInteger + 1))
        total = sum(choices)
        if total < desiredTotal:
            return False
        if total == desiredTotal and maxChoosableInteger % 2 == 1:
            return True
        table = {}

        def helper(choices_remain, target):
            if not choices_remain:
                return False
            if choices_remain[-1] >= target:
                return True
            key = tuple(choices_remain)
            if key in table:
                return table[key]
            for i in range(len(choices_remain)):
                if not helper(choices_remain[:i] + choices_remain[i + 1:], target - choices_remain[i]):
                    table[key] = True
                    return True
            table[key] = False
            return False

        return helper(choices, desiredTotal)
