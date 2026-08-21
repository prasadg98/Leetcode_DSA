class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]

        n = len(nums)
        loot = [0] * n

        loot[0] = nums[0]
        loot[1] = max(nums[0], nums[1])

        for i in range(2,n):
            loot[i] = max(loot[i-2] + nums[i], loot[i-1])

        return loot[-1]

        






        