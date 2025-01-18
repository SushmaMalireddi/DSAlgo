class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=0
        max=-sys.maxsize-1
        for i in nums:
            summ+=i
            if(summ>max):
                max=summ
            if(summ<0):
                summ=0
        return max