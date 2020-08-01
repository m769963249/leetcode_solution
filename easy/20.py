class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) %2 !=0:
            return False
        if len(s) =="":
            return True
        char_map = {"[":"]","{":"}","(":")"}
        stack = []
        for c in s:
            if c in char_map:
                stack.append(c)
            else:
                if len(stack)>0:
                    if char_map[stack.pop()] != c:
                        return False
        return len(stack)==0
    #递归消除，最简单的方法
    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.__contains__("{}") or s.__contains__("[]") or s.__contains__("()"):
            return self.isValid(s.replace("{}","").replace("[]","").replace("()",""))
        else:
            return s == ""




if __name__ == "__main__":
    solution = Solution()
    # s = "()"
    # s = "()[]{}"
    # s = "(]"
    # s = "){"
    s = "(([]){})"
    result = solution.isValid(s=s)
    print(type(result))
    print(str(result))
