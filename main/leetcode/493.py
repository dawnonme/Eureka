''' Reverse Pairs '''


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ''' Modified Merge Sort: Time: O(nlogn), Space: O(n)
        Idea:
        '''
        if not nums:
            return 0

        return self.merge_sort_and_count(nums, 0, len(nums) - 1)

    def merge_sort_and_count(self, nums, lo, hi):
        if lo >= hi:
            return 0
        mid = (lo + hi) // 2
        cnt = 0

        cnt += self.merge_sort_and_count(nums, lo, mid)
        cnt += self.merge_sort_and_count(nums, mid + 1, hi)

        sl, sh = lo, mid + 1
        while sl <= mid and sh <= hi:
            if nums[sl] > 2 * nums[sh]:
                cnt += (mid - sl + 1)
                sh += 1
            else:
                sl += 1
        nums[lo:hi + 1] = sorted(nums[lo:hi + 1])
        return cnt
