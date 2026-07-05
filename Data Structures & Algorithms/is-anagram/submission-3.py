class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        for st in s:
            if st not in countS:
                countS[st] = 1
            else:
                countS[st] += 1

        for tt in t:
            if t not in countT:
                countT[tt] = 1
            else:
                countT[tt] += 1

        return countS == countT