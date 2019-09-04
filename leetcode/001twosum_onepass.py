class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i, v in enumerate(nums):
            remain = target - v
            if remain in record:
                return [record[remain],i]
            else:  
                record[v] = i
        