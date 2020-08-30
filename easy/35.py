class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if nums[0] > target:
            return 0
        for i in range(0, len(nums)):
            if target == nums[i]:
                return i
            elif target < nums[i]:
                return i
        else:
            return len(nums)


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 3, 4, 5]
    # nums = "english"
    target = 2
    result = solution.searchInsert(nums=nums, target=target)
    print(type(result))
    print(str(result))
