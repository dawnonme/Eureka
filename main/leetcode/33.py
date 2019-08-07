class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums, self.target = nums, target
        return self.binary_search_rot(0, len(nums) - 1)

    def binary_search_rot(self, lo, hi):
        if lo > hi:
            return -1

        mid = (lo + hi) // 2
        if self.nums[mid] == self.target:
            return mid

        if self.nums[hi] > self.nums[lo]:
            if self.target > self.nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        elif self.nums[hi] < self.nums[lo]:
            if self.nums[mid] >= self.nums[lo]:
                if self.target > self.nums[mid]:
                    lo = mid + 1
                else:
                    if self.target > self.nums[hi]:
                        hi = mid - 1
                    elif self.target < self.nums[hi]:
                        lo = mid + 1
                    else:
                        return hi

            elif self.nums[mid] <= self.nums[hi]:
                if self.target > self.nums[mid]:
                    if self.target > self.nums[lo]:
                        hi = mid - 1
                    elif self.target < self.nums[lo]:
                        lo = mid + 1
                    else:
                        return lo
                else:
                    hi = mid - 1

            else:
                return -1

        else:
            return -1

        return self.binary_search_rot(lo, hi)
