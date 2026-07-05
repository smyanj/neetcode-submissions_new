class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        isAn = set()
        isAn_t = set()
        for c in s:
            if c not in isAn:
                isAn.add(c)
        
        for c in t:
            if c not in isAn_t:
                isAn_t.add(c)
            
        print(isAn)
        print(isAn_t)

        return isAn == isAn_t
