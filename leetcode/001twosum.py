class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leng = len(nums)
        for i in range(0, leng):
            max_distance = leng - i
            for distance in range(1, max_distance):
                if nums[i]+nums[i+distance]==target:
                    return [i,i+distance]
            
        