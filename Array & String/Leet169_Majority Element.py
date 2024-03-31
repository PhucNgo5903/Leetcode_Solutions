169. Majority Element
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, cnt = nums[0], 0         #candidate = nums[0], count = 0
        for v in nums:
            if v == candidate:
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                candidate = v
                cnt = 1
        
        return candidate