class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:

        l,ml,zc = 0,0,0

        for r in range(len(nums)):
            if nums[r] == 0:
                zc += 1

            while zc > k:
                if nums[l] == 0:
                    zc -= 1
                l += 1

            ml = max(ml,r - l + 1)

        return ml
        