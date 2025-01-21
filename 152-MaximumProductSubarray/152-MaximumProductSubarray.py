class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=float(-inf)
        n=len(nums)
        prefix=1
        suffix=1
        for i in range(n):
            if prefix==0: prefix=1
            if suffix==0: suffix=1
            prefix*=nums[i]
            suffix*=nums[n-i-1]
            print("ore",prefix,"suf",suffix,"maxi",maxi)
            maxi=max(maxi,max(prefix,suffix))
        return maxi


