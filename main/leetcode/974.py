class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = cur_sum = 0
        prev_sum = K * [0]
        prev_sum[0] = 1

        for num in A:
            cur_sum += num
            cur_sum %= K
            ans += prev_sum[cur_sum]
            prev_sum[cur_sum] += 1
        return ans
