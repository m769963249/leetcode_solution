class Solution:
    def countAndSay(self, n: int) -> str:
        list_str = "1"
        for i in range(n-1):
            x = 0
            tmp = ""
            for index in range(len(list_str)):
                if list_str[x] != list_str[index]:
                    tmp = tmp + str(index-x) + list_str[x]
                    x = index
            list_str = tmp + str(len(list_str)-x) + list_str[-1]
        return list_str


if __name__ == "__main__":
    solution = Solution()
    target = 5
    result = solution.countAndSay(n=target)
    print(type(result))
    print(str(result))
