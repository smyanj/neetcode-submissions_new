class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in indicies:
                return [indicies[diff], i]
            indicies[v] = i

        