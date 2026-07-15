class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            secondnum = target - num
            if secondnum in seen:
                return [seen[secondnum], i]
            seen[num] = i
            
            
                






        