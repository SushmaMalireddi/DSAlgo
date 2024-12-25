class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=set(nums)
        longest=0
        for i in ans:
            if i-1 not in ans:
                count=0
                smallest=i
                while smallest in ans:
                    count+=1
                    smallest+=1
                longest=max(count,longest)
        return longest