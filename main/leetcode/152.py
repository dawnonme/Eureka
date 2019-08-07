class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp_max = [nums[0]]
        dp_min = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] >= 0:
                dp_max.append(max(nums[i], dp_max[i - 1] * nums[i]))
                dp_min.append(min(nums[i], dp_min[i - 1] * nums[i]))
            else:
                dp_max.append(max(nums[i], dp_min[i - 1] * nums[i]))
                dp_min.append(min(nums[i], dp_max[i - 1] * nums[i]))

        return max(dp_max)

    def maxProductConstantSpace(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        last_max = last_min = overall_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] >= 0:
                this_max = max(nums[i], nums[i] * last_max)
                this_min = min(nums[i], nums[i] * last_min)
            else:
                this_max = max(nums[i], nums[i] * last_min)
                this_min = min(nums[i], nums[i] * last_max)

            last_max, last_min = this_max, this_min
            overall_max = max(overall_max, last_max)

        return overall_max