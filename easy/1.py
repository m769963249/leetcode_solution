class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for index, num in enumerate(nums):
            if dict1.__contains__(target - num):
                return [dict1.get(target - num), index]
            dict1[num] = index


if __name__ == "__main__":
    solution = Solution()
    list1 = [1, 1, 5, 7, 9]
    target = 2
    result = solution.twoSum(nums=list1, target=target)
    print(str(result))
