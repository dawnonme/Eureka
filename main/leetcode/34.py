# class Solution:
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         output = []
#         output.append(self.binarySearch(nums, target, 0, len(nums) - 1, False))
#         output.append(self.binarySearch(nums, target, 0, len(nums) - 1, True))
#         return output

#     def binarySearch(self, nums, target, l, r, reverse):
#         if l <= r:
#             mid = int((l + r) / 2)
#             if nums[mid] > target:
#                 return self.binarySearch(nums, target, l, mid - 1, reverse)
#             elif nums[mid] < target:
#                 return self.binarySearch(nums, target, mid + 1, r, reverse)
#             elif not reverse:
#                 if mid == 0 or nums[mid - 1] != target:
#                     return mid
#                 else:
#                     return self.binarySearch(nums, target, l, mid - 1, reverse)
#             elif reverse:
#                 if mid == len(nums) - 1 or nums[mid + 1] != target:
#                     return mid
#                 else:
#                     return self.binarySearch(nums, target, mid + 1, r, reverse)
#         return -1


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = self.binarySearch(nums, target)
        if idx == -1:
            return [-1, -1]
        start = end = idx
        while start - 1 >= 0 and nums[start - 1] == target:
            start -= 1
        while end + 1 < len(nums) and nums[end + 1] == target:
            end += 1
        return [start, end]

    def binarySearch(self, nums, target):
        return self.__binarySearch(nums, target, 0, len(nums) - 1)

    def __binarySearch(self, nums, target, l, r):
        if l > r:
            return -1
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid - 1
            return self.__binarySearch(nums, target, l, r)
        elif nums[mid] < target:
            l = mid + 1
            return self.__binarySearch(nums, target, l, r)
        else:
            return mid
