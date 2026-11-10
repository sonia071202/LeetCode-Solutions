class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        window = 0
        left = 0
        ans = float('inf')

        


        for right in range(len(nums)):
            window += nums[right]

            while window >= target:
                ans = min(ans, right - left + 1)

                window -= nums[left]
                left +=1

            

        if ans == float('inf'):
                return 0

        return ans
        