class Solution(object):
    def countMaxOrSubsets(self, nums):
        a = [0] * (1 << 17)
        a[0] = 1
        max_or = 0
        for num in nums:
            for i in range(max_or, -1, -1):
                a[i | num] += a[i]
            max_or |= num
        return a[max_or]
        