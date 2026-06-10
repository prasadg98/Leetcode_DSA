class Solution:
   def minimumCost(self, nums: List[int]) -> int:
    first_cost = nums[0]
    minimum = float('inf')
    second_min = float('inf')

    for i in range(1, len(nums)):
        if nums[i] <= minimum:
            second_min = minimum
            minimum = nums[i]
        elif nums[i] < second_min:
            second_min = nums[i]

    return first_cost + minimum + second_min


            

