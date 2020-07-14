class Solution(object):
    # my solution
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        transform_code_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for index in range(len(s) - 1):
            if transform_code_table[s[index + 1]] > \
                    transform_code_table[s[index]]:
                result = result - transform_code_table[s[index]]
            else:
                result = result + transform_code_table[s[index]]
        return result + transform_code_table[s[len(s) - 1]]


if __name__ == "__main__":
    solution = Solution()
    rom_number = "III"
    # rom_number = "MCMXCIV"
    result = solution.romanToInt(s=rom_number)
    print(type(result))
    print(str(result))
