class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        for i in range(0,len(haystack)):
            if haystack[i] is needle[0] and haystack[i:len(needle)+i] == needle:
                index = i
                return i
        else:
            return -1


if __name__ == "__main__":
    solution = Solution()
    # l1 = [0, 0, 1, 1, 2, 2, 2, 3, 4, 4, 5]
    haystack = "english"
    needle = "ng"
    result = solution.strStr(haystack=haystack, needle=needle)
    print(type(result))
    print(str(result))
