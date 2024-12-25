class Solution:
    def reverse(self,nL,start,end):
        while start < end:
            nL[start], nL[end] = nL[end], nL[start]
            start += 1
            end -= 1
        print(nL,"its new list")
        return nL

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=-1
        n=len(nums)
        for i in range (n-2,-1,-1):
            if(nums[i]<nums[i+1]):
                ind=i
                break

        if ind==-1:
            nums.reverse()
            return nums

        for j in range(n-1,ind,-1):
            if(nums[j]>nums[ind]):
                break
        nums[ind],nums[j]=nums[j],nums[ind]

        return self.reverse(nums,i+1,n-1)



        