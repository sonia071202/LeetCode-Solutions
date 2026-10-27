class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        
        
        left = 0
        count = 0
        odd = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd +=1
                count = 0
                

            while odd == k:
                if nums[left] % 2 == 1:
                    odd-=1

                left += 1
                count += 1

            ans += count

        return ans