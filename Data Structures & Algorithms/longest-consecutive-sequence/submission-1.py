class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)

        for n in nums:
            streak, curr = 0, n

            while curr in numsSet:
                curr += 1
                streak += 1
                
            res = max(res, streak)

        return res