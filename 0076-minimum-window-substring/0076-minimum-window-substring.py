class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        mpp = {}
        for ch in t:
            mpp[ch] = mpp.get(ch,0) + 1


        l = 0
        start = 0
        count = len(t)
        minlen = float('inf')

        for r in range(len(s)):
            if mpp.get(s[r],0) > 0:
                count -= 1

            mpp[s[r]] = mpp.get(s[r],0) - 1

            while count == 0:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    start = l

                mpp[s[l]] += 1

                if mpp[s[l]] > 0:
                    count += 1

                l += 1

        return "" if minlen == float('inf') else s[start:start + minlen] 
                    



