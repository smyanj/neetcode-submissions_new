class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        l, output = 0, ""
        currLongest = float('inf')
        have, need = 0, len(set(t))
        windowC, tC = {}, {}
        for i in range(len(t)):
            tC[t[i]] = 1 + tC.get(t[i], 0)

        for r in range(len(s)):
            windowC[s[r]] = 1 + windowC.get(s[r], 0)
            
            if s[r] in tC and windowC[s[r]] == tC[s[r]]:
                have += 1
                while have == need:
                    if r - l + 1 < currLongest:
                        currLongest = r - l + 1
                        output = s[l:r+1]

                    windowC[s[l]] -= 1
                    if s[l] in tC and windowC[s[l]] < tC[s[l]]:
                        have -= 1
                    l += 1

        return output