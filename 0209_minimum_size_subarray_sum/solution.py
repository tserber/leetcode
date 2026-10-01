class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_length = float('inf')
        curSum = 0
        l = 0

        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                min_length = min(min_length, r - l + 1)
                curSum -= nums[l]
                l += 1

        return min_length if min_length != float('inf') else 0
