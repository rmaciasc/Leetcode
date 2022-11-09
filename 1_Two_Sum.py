class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        already_seen = {}
        for i, num in enumerate(nums): 
            remain = target - num
            if remain in already_seen:
                return [i, already_seen[remain]]
            already_seen[num] = i
        return None

sol = Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums, target))