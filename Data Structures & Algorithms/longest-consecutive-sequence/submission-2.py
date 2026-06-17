class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        nums.sort()

        n = len(nums)
        curr, streak = nums[0], 0
        i = 0

        while i < n:
            if curr != nums[i]:
                curr = nums[i]
                streak = 0

            while i < n and nums[i] == curr:
                i += 1

            streak += 1
            curr += 1
            res = max(res, streak)

        return res
