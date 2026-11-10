class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        left = 0
        maxi = float('-inf')
        
        window = 0

        for right in range(len(nums)):
            window += nums[right]

            if right - left + 1 == k:

                curr_max = max(maxi,window/k)
                maxi = curr_max

            

                window -= nums[left]
                left += 1

        return maxi        