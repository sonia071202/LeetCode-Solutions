class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        freq = {}

        for x in nums:
            freq[x] = freq.get(x,0) + 1

        return max(freq,key=freq.get)
        