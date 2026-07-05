class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashset = {}
         for nu in nums:
            if nu not in hashset:
                hashset[nu] = 1
            else:
                hashset[nu] += 1
        
         for ha in hashset:
            if hashset[nu] > 1:
                return True

         return False