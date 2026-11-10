class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        count = 0
        curr_sum = 0

        for x in nums:
            curr_sum += x

            needed = curr_sum - k

            count += freq.get(needed,0)

            freq[curr_sum] = freq.get(curr_sum,0) + 1

        return count
        