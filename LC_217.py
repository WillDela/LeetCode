class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: 
                return True
        else: return False  


# first leetcode problem and went with a brute force solution 

# O(n log n), most optimal solution would be O(n) but getting there little by little