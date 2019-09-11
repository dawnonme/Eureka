class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        next_idx = lambda idx: (idx + nums[idx]) % len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            positive = nums[i] > 0
            slow, fast = i, next_idx(i)

            while ((nums[fast] > 0 and positive) or (nums[fast] < 0 and not positive)) and \
                  ((nums[next_idx(fast)] > 0 and positive) or (nums[next_idx(fast)] < 0 and not positive)):
                if slow == fast:
                    if slow == next_idx(slow):
                        break
                    return True

                slow = next_idx(slow)
                fast = next_idx(next_idx(fast))

            tmp = i

            while (nums[tmp] > 0 and positive) or (nums[tmp] < 0
                                                   and not positive):
                next_tmp = next_idx(tmp)
                nums[tmp] = 0
                tmp = next_tmp

        return False
