class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        newS = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                newS += c

        l, r = 0, len(newS) - 1
        newS = newS.lower()
        while l <= r:
            if newS[l] != newS[r]:
                return False

            l += 1
            r -= 1

        return True