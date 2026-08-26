class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        streak = 0
        l, r = 0, 0

        for n in nums:
            if (n - 1) not in values:
                length = 0
                while (n + length) in values:
                    length += 1
                streak = max(streak, length)

        return streak