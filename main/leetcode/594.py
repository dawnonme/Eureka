class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        max_len = 0
        for num in nums_dict:
            if num + 1 in nums_dict:
                max_len = max(max_len, nums_dict[num] + nums_dict[num + 1])
        return max_len
