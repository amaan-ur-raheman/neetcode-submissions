class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        n = len(heights)

        for l in range(n):
            for r in range(l + 1, n):
                area = (r - l) * min(heights[r], heights[l])
                result = max(result, area)

        return result