"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count={}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=i
            elif nums[i] in count and abs(count[nums[i]]-i)<=k:
                return True
            else:
                count[nums[i]]=i
        return False