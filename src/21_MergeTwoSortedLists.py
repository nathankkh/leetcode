from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# merge two sorted lists
# return the head of the merged linked list
# final list must be sorted
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
            
        # res = ListNode()

        
        # if not list1.val:
        #     return list2
        # if not list2.val:
        #     return list1
        
        # if list1.val > list2.val:
        #     res.val = list2.val
        #     list2 = list2.next
        # else:
        #     res.val = list1.val
        #     list1 = list1.next
        
        # tail = res
        # while True:
        #     if not list1 and list2:
        #         break
        #     # if other has no value, just append all of the initial list
        #     if not list1:
        #         while list2:
        #             tail.next = ListNode(list2.val)
        #             list2 = list2.next
        #             tail = tail.next
        #         break
        #     elif not list2:
        #         while list1:
        #             tail.next = ListNode(list1.val)
        #             list1 = list1.next
        #             tail = tail.next
        #         break
            
        #     if list1.val < list2.val:
        #         tail.next = ListNode(list1.val)
        #         list1 = list1.next
        #         tail = tail.next
        #     else:
        #         tail.next = ListNode(list2.val)
        #         list2 = list2.next
        #         tail = tail.next
        
        # return res

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))