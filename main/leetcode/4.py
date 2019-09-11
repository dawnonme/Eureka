''' Median of Two Sorted Arrays '''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """ Merge: Time: O((m + n) / 2), Space: O(1)
        """
        num_ele = len(nums1) + len(nums2)
        num_merged, last_merged = 0, 0
        p1, p2 = 0, 0

        even = (num_ele % 2 == 0)
        target = num_ele / 2

        while num_merged < target:
            if p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    last_merged = nums1[p1]
                    p1 += 1
                else:
                    last_merged = nums2[p2]
                    p2 += 1
            elif p1 < len(nums1):
                last_merged = nums1[p1]
                p1 += 1
            else:
                last_merged = nums2[p2]
                p2 += 1
            num_merged += 1

        median = last_merged

        if even:
            if p1 < len(nums1) and p2 < len(nums2):
                next_merged = min(nums1[p1], nums2[p2])
            elif p1 < len(nums1):
                next_merged = nums1[p1]
            else:
                next_merged = nums2[p2]
            median = (median + next_merged) / 2

        return median

    def find_median_sorted_arrays(self, nums1, nums2):
        ''' Mathematical Method: Time: O(log(m+n))
        '''
        # TODO
        pass