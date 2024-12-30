class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        runningSum=0
        store={0:1}
        count=0
        for i in nums:
            runningSum+=i
            if  runningSum-k in store:
                count+=store[runningSum-k]

            if runningSum in store : 
                store[runningSum]+=1
            else:
                store[runningSum]=1          

        return count