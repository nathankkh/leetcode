from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        res = ListNode(head.val)
        head = head.next
        # print("starting", check(res))
        while head != None:
            curr = res
            res = ListNode(head.val, curr)
            head = head.next
            # print(check(res))
        return res

    def reverseListInPlace(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        curr = head

        while curr:
            temp = curr.next # store the next listnode
            curr.next = prev # change to whatever's been appended so far
            prev = curr
            curr = temp
        
        return prev


def check(lst):
    while lst != None:
        print(lst.val)
        lst = lst.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
