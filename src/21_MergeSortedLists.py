# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while True:
            if not list1:
                while list2:
                    temp.append(list2.val)
                    list2 = list2.next
                break
            if not list2:
                while list1:
                    temp.append(list1.val)
                    list1 = list1.next
                break
            
            if list1.val > list2.val:
                temp.append(list2.val)
                list2 = list2.next
            else:
                temp.append(list1.val)
                list1 = list1.next

        res = tail = ListNode()
        for i in temp:
            res.next = ListNode(i)
            res = res.next
        return tail.next