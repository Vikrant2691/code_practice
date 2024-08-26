from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res_list = ListNode()
        curr = res_list
        
        while list1 != None and list2 != None:
            if list1.val<list2.val:
                new_node = ListNode()
                new_node.val = list1.val
                curr.next=new_node
                curr=curr.next
                list1=list1.next
            else:
                new_node = ListNode()
                new_node.val = list2.val
                curr.next=new_node
                curr=curr.next
                list2=list2.next
        
        while list1 != None:
            new_node = ListNode()
            new_node.val = list1.val
            curr.next=new_node
            curr=curr.next
            list1=list1.next
        
        while list2 != None:
            new_node = ListNode()
            new_node.val = list2.val
            curr.next=new_node
            curr=curr.next
            list2=list2.next

        return res_list.next