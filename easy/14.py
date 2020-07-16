class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        length = len(strs[0])
        count = len(strs)
        for i in range(length):
            point = strs[0][i]
            for j in range(1, count):
                if i == len(strs[j]) or strs[j][i] != point:
                    return strs[0][:i]
        return strs[0]

    def longestCommonPrefix2(self, strs):
        if not strs:
            return ""
        length = len(strs[0])
        count = len(strs)
        for i in range(length):
            point = strs[0][i]
            if any(i == len(strs[j]) or strs[j] != point for j in range(1, count)):
                return strs[0][:i]
        return strs[0]


if __name__ == "__main__":
    solution = Solution()
    rom_number = ["c", "c", "c"]
    result = solution.longestCommonPrefix2(strs=rom_number)
    print(type(result))
    print(str(result))
