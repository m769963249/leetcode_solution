class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        move = result
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next

        move.next = l1 if l1 else l2

        return result.next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l2 = ListNode(2)
    l2.next = ListNode(4)
    result = solution.mergeTwoLists(l1=l1, l2=l2)
    while result:
        print(result.val)
        result = result.next
    print(type(result))
    print(str(result))
