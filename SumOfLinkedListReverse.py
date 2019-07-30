# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    # [3] -> [1] -> [6]
    # [1] -> [1] -> [2]
    # -------------------
    # [4]    [2]    [8]

    # Solution  -> 824

    # 12 MB [Run 1: 60 ms, Run 2: 56 ms]
    def addTwoNumbers(self, l1, l2, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if l1.next != None or l2.next != None or c != 0:
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret

    # What's really interesting is that using operators uses less space and time than
    # using is/is not statements
    # 12 MB
    # 52 ms
    def addTwoNumbersTest(self, l1, l2, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret