class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        idx = 0

        while idx < len(points):
            
