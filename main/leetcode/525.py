class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table = {0: -1}
        cnt = ans = 0

        for i, num in enumerate(nums):
            cnt += 1 if num == 1 else -1
            if cnt not in table:
                table[cnt] = i
            else:
                ans = max(ans, i - table[cnt])
        
        return ans