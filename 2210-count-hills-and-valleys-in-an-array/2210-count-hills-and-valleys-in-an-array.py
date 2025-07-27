class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nums = [item[0] for item in itertools.groupby(nums)]
    
        count = 0
        for i in range(1, len(nums)-1):
            if (nums[i] > nums[i-1] and nums[i] > nums[i+1]) or (nums[i] < nums[i-1] and nums[i] < nums[i+1]):    
                count += 1
        return count            