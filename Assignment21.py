from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        if t < 0:
            return False

        n = len(nums)
        num_arr = []
        for i in range(n):
            temp = (nums[i],i)
            num_arr.append(temp)

        num_arr = sorted(num_arr)

        for i in range(n):

            for j in range(i+1,n):
                
                if abs(num_arr[i][0] - num_arr[j][0]) <= t :
                   
                    if abs(num_arr[i][1] - num_arr[j][1]) <= k:
                        
                        return True
                else:
                    break
        return False

print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))