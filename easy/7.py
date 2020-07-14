class Solution(object):
    # my solution
    def reverse_int_num(self, x):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            str1 = str(x)[::-1]
            if str1.__contains__("-"):
                str1 = "-" + str1.replace("-", "")
                return 0 if int(str1) < -2147483648 else int(str1)
            else:
                return 0 if int(str1) > 2147483647 else int(str1)
        except Exception:
            return 0

    # best solution
    def reverse_int_num2(self, x):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = 0
        while (x != 0):
            if x > 0:
                temp = x % 10
                x = x // 10
            if x < 0:
                temp = x % -10
                x = -(x // -10)
            result = result * 10 + temp
        if (result > 0 and result > 2147483647):
            return 0
        if (result < 0) and (result < -2147483648):
            return 0
        return result


if __name__ == "__main__":
    solution = Solution()
    num = 1534236469
    # num = -123
    # result = solution.reverse_int_num(x=num)
    result = solution.reverse_int_num2(x=num)
    print(type(result))
    print(str(result))
