class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        uniq = 0
        for curr in range(0, len(nums)):
            if nums[curr] != nums[uniq]:
                uniq = uniq + 1
                nums[uniq] = nums[curr]
        return uniq + 1