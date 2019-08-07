class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        dpl, dpr = [1] * len(nums), [1] * len(nums)
        mul = 1
        for i in range(len(nums)):
            dpl[i] = mul
            mul *= nums[i]
        mul = 1
        for i in range(len(nums) - 1, -1, -1):
            dpr[i] = mul
            mul *= nums[i]
        for i in range(len(nums)):
            prod = dpl[i] * dpr[i]
            res.append(prod)
        return res

    def productExceptSelfConstantSpace(self, nums: List[int]) -> List[int]:
        res = [1] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        mul = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= mul
            mul *= nums[i]
        return res
