class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}

        for i, v in enumerate(nums):
            indicies[v] = i

        for i, v in enumerate(nums):
            diff = target - v
            if diff in indicies and indicies[diff] != i:
                return [i, indicies[diff]]

        