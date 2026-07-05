class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        perm = set(s1)
        matches = 0

        if s1 == s2:
            return True

        for r in range(len(s2)):
            if s2[r] in perm:
                matches += 1
                
        print(r-l + 1)
        return len(s1) == matches


