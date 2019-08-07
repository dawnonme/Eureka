class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ''' Better Brute Force: Time: O(n^2), Space: O(1)
        '''
        min_fst = float('inf')
        for snd in range(1, len(nums) - 1):
            min_fst = min(min_fst, nums[snd - 1])
            for trd in range(snd + 1, len(nums)):
                if nums[snd] > nums[trd] and nums[trd] > min_fst:
                    return True
        return False

    def find_132_pattern(self, nums):
        ''' Stack: Time: O(n), Space: O(n)
        Idea: Use a stack to keep track of the 3 elements.
        '''
        ele, stack = -float('inf'), []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < ele:
                return True
            while stack and stack[-1] < nums[i]:
                ele = stack.pop()
            stack.append(nums[i])
        return False