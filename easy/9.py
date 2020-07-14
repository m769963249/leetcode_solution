class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x)[::-1] == str(x):
            return True
        else:
            return False

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        result = 0
        x_box = x
        if x < 0:
            return False
        while x > 0:
            mod = x % 10
            x = x / 10
            result = result * 10 + mod
        return True if result == x_box else False


if __name__ == "__main__":
    solution = Solution()
    # num = 1534236469
    num = 121
    # result = solution.isPalindrome(x=num)
    result = solution.isPalindrome2(x=num)
    print(type(result))
    print(str(result))
