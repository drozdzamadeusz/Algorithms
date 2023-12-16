from typing import List


class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    
    slow, fast = 0,0
    while True:
      slow = nums[slow]
      fast = nums[nums[fast]]

      if slow == fast:
          break

    slow2 = 0

    while slow != slow2:
      slow = nums[slow]
      slow2 = nums[slow2]

    return slow2
  

sol = Solution().findDuplicate([1,3,4,2,2])
print(sol)