class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r = 0, 1
        dupes, longest = set(), 0

        for r in range(1, len(s)):
            if s[l] not in dupes and s[l] != s[r]:
                curr = s[l:r+1]
                longest = max(longest, len(curr))
                dupes.add(s[l])

        return longest + 1