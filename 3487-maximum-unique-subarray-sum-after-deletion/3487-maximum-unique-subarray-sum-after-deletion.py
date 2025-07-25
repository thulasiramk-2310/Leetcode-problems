class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s,a=set(),set()
        for i in nums:
            if i>0:
                s.add(i)
            else:
                a.add(i)
        return sum(s) if len(s)>0 else max(a)