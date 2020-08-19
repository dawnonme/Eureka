class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_arr = [float("-inf"), float("-inf"), float("-inf")]
        for n in nums:
            if n in max_arr:
                continue

            if n > max_arr[2]:
                max_arr[0] = max_arr[1]
                max_arr[1] = max_arr[2]
                max_arr[2] = n
            elif n > max_arr[1]:
                max_arr[0] = max_arr[1]
                max_arr[1] = n
            elif n > max_arr[0]:
                max_arr[0] = n

        return max_arr[0] if max_arr[0] != float("-inf") else max_arr[2]
