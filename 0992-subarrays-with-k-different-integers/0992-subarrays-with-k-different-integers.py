class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:

        def atMostK(nums,k):
            left = 0
            count = 0
            mpp = {}

            for  right in range(len(nums)):
                mpp[nums[right]] = mpp.get(nums[right],0) + 1

                while len(mpp) > k:
                    mpp[nums[left]] -= 1

                    if mpp[nums[left]] == 0:
                        del mpp[nums[left]]

                    left += 1
                count += right - left + 1

            return count
        
        return atMostK(nums,k) - atMostK(nums,k-1)