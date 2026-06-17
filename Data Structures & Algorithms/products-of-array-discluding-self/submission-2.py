class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod, zero_cnt = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1

        if zero_cnt > 1: return [0] * n

        res = [0] * n
        for i, c in enumerate(nums):
            if zero_cnt: 
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c

        return res
