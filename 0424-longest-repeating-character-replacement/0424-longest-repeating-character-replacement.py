class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxlen = 0 
        l = 0
        r = 0 
        mpp = {}

        n = len(s)
        maxfreq = 0

        while r < n:
            mpp[s[r]] = mpp.get(s[r], 0) + 1
            maxfreq = max(maxfreq, mpp[s[r]])

            while  (r - l + 1) - maxfreq > k:
                mpp[s[l]] -= 1 
                l += 1

            maxlen = max(maxlen, r - l + 1)
            r += 1

        return maxlen

            