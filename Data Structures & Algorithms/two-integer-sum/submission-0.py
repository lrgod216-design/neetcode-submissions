class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            number = nums[i]
            desired = target - number
            if desired in seen:
                return[seen[desired], i]
            seen[number] = i
        return None
        