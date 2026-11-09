class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        

        seen = set(nums)

        longest = 0

        

        for x in seen:
            if x - 1 not in seen:
                count = 1


                while x + count in seen:
                    count += 1

                longest = max(longest,count)

        return longest



        