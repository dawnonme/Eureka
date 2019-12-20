class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)

        for i in range(1, num + 1):
            if (i - 1) % 2 == 0:
                dp[i] = dp[i - 1] + 1
            else:
                tmp = (i - 1) >> 1
                num_ones = dp[i - 1] - 1
                while tmp % 2 == 1:
                    num_ones -= 1
                    tmp >>= 1
                num_ones += 1
                dp[i] = num_ones

        return dp

    def count_bits(self, num):
        output = [0]
        for i in range(1, num + 1):
            a = output[i // 2] + (i % 2)
            output.append(a)

        return output
