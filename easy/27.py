class Solution:

    # execute time out
    def removeElement(self, nums, val):
        if not nums:
            return 0
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == val:
                i = i + 1
            else:
                nums[j] = nums[i]
                i = i + 1
                j = j + 1
        print(nums)
        return j


if __name__ == "__main__":
    solution = Solution()
    # l1 = [0, 0, 1, 1, 2, 2, 2, 3, 4, 4, 5]
    l1 = [3, 2, 2, 3]
    val = 3
    result = solution.removeElement(nums=l1, val=val)
    print(result)
    print(type(result))
    print(str(result))
