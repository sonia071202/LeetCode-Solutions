class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        if not nums:
            return 0

        best = nums[0]
        curr = nums[0]

        for i in range(1,len(nums)):
            curr = max(nums[i], curr + nums[i])
            best = max(best,curr)

        return best
        