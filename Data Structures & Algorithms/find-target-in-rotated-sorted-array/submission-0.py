class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            
            if nums[m] > nums[l] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
            
            if nums[m] < nums[r] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
        return -1

            
            

        return idx

