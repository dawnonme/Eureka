class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = {0: 1}
        cnt = ans = 0

        for num in nums:
            cnt += num
            if cnt - k in table:
                ans += table[cnt - k]

            if cnt in table:
                table[cnt] += 1
            else:
                table[cnt] = 1

        return ans