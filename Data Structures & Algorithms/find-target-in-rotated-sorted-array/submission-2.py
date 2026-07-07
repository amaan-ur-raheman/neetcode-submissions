class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        def binary_search(l: int, r: int) -> int:
            while l <= r:
                m = l + (r - l) // 2

                if target == nums[m]:
                    return m
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        
        return binary_search(pivot, len(nums) - 1)