class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxcal(nums):
            ans = [0] * len(nums)
            ans[0] = nums[0]
            ans[1] = max(nums[0],nums[1])
            for i in range(2, len(nums)):
                ans[i] = max(ans[i-2]+ nums[i], ans[i-1])
            
            return ans[-1]

        n = len(nums)
        if n < 2:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        firstselected = nums[:n-1]
        lastselected = nums[1:n]

        max_first_selected = maxcal(firstselected)
        max_last_selected = maxcal(lastselected)

        return max(max_first_selected,max_last_selected)

        



        