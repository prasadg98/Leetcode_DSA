class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxcount = 0
        for num in nums:
            if num == 1:
                counter = counter + 1
                maxcount = max(maxcount,counter)
            else:
        
                counter = 0
        
        return maxcount