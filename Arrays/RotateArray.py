from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums: List[int], a: int, b: int):
            while a <= b:
                temp = nums[a]
                nums[a] = nums[b]
                nums[b] = temp
                a += 1
                b -= 1
            return nums

        k = k % len(nums)
        reverse(nums, 0, (len(nums) - k) - 1)
        reverse(nums, len(nums) - k, len(nums) - 1)
        reverse(nums, 0, len(nums) - 1)

# Test the solution locally
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]  # Example input
    k = 3  # Example rotation value
    print("Original:", nums)
    Solution().rotate(nums, k)
    print("Rotated:", nums)
