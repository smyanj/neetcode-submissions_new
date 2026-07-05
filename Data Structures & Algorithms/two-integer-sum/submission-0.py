class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 1

        for i, v in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if nums[j] + v == target:
                    return [i, j]