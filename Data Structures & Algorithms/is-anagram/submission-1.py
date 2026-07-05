class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashAn = {}
        for c in s:
            if c not in hashAn:
                hashAn[c] = 1
            else:
                hashAn[c] += 1
        
        for c in t:
            if c not in hashAn:
                return False
        return True
