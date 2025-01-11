class Solution:
    def search(self, nums: List[int], target: int, low: int=None, high: int=None) -> int:
        if low is None or high is None:
            low=0
            high=len(nums)-1
        if low>high:
            return -1
        mid=(low + high)//2
        #print("mid is", mid)
        if target==nums[mid]:
            #print("target found", mid)
            return mid
        else:
            if target>=nums[mid]:
                return self.search(nums,target,mid+1,high)
            else:
                return self.search(nums,target,low,mid-1)
        return -1