class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        seen = {}

        for i,x in enumerate(nums):
            needed = target - x

            if needed in seen:
                return [seen[needed],i]

            seen[x] = i

        