class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ''' Brute Force + Sort: Time( O(n^2 * 2logn) ), Space: ( O(n^2) )  
        '''
        temp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp.append(matrix[i][j])
        temp.sort()
        return temp[k - 1]

    def kth_smallest_binary_search(self, matrix, k):
        ''' Binary Search
        Idea: Count the number of elements that are smaller that this element.
        '''

        def count_smaller(m, x):
            i, j, count = 0, len(m) - 1, 0
            while i < len(m) and j >= 0:
                if m[i][j] > x:
                    j -= 1
                else:
                    count += (j + 1)
                    i += 1
            return count

        lo, hi = matrix[0][0], matrix[-1][-1]

        while lo < hi:
            mid = (lo + hi) // 2
            if count_smaller(matrix, mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return hi