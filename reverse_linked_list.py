from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def create_linked_list(self, arr:List):
        head = ListNode()
        curr = head
        for a in arr:
            new_node = ListNode()
            new_node.val=a
            curr.next = new_node
            curr = curr.next
        return head.next
    
    def print_linked_list(self, head):
        curr = head
        while curr != None:
            print(curr.val)
            curr= curr.next
            

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr!=None:
            temp = curr.next
            curr.next= prev
            prev = curr
            curr= temp
        
        return prev
    
head = ListNode().create_linked_list([1,2,3,4])
rev_head = Solution().reverseList(head)
ListNode().print_linked_list(rev_head)


        
        