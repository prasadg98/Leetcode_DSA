class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            second_num = target - num
            if second_num in seen:
                return [seen[second_num], i]
            else:
                seen[num] = i            
                






        