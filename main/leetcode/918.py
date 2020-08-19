class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]

        sum_A = A[0]
        max_sub_sum = A[0]
        min_sub_sum = A[0]

        last_max = A[0]
        last_min = A[0]

        for i in range(1, len(A)):
            sum_A += A[i]

            if max_arr_sum[i - 1] > 0:   
                last_max += A[i]         
                max_sub_sum = max(max_sub_sum, last_max)
            last_max = A[i]

            if i == len(A) - 1:
                break
            
            if min_arr_sum[i - 1] < 0:
                min_arr_sum[i] += min_arr_sum[i - 1]

            min_sub_sum = min(min_sub_sum, min_arr_sum[i])

        return max(max_sub_sum, sum_A - min_sub_sum)

