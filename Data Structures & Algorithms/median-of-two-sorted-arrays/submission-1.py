class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        merged = nums1 + nums2
        merged.sort()

        total = len(merged)

        if total % 2:
            return merged[total // 2]
        else:
            return (merged[total // 2 - 1] + merged[total // 2]) / 2.0