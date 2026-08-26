class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        streak, length = 0, 0
        for n in nums:
            if n - 1 not in unique:
                length = 0
            while n + length in unique:
                length += 1
            streak = max(streak, length)

        return streak