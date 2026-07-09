class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        best = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            elif nums[i] == 0:
                cur = 0
            best = max(best, cur)
        return best
            
        
           
                