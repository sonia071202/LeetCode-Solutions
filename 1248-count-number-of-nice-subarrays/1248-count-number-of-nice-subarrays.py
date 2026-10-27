class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        
        def at_most(k):
            left = 0
            count = 0
            odd = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd +=1
                

                while odd > k:
                    if nums[left] % 2 == 1:
                        odd-=1

                    left += 1

                count += right - left + 1

            return count

        return at_most(k) - at_most(k-1)