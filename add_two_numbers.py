from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        l1_h = l1
        l2_h = l2
        c=0
        curr = l3
        while l1_h and l2_h:
            new_node= ListNode()
            r = l1_h.val + l2_h.val + c
            c=0
            if r >= 10:
                c = r//10
                new_node.val = r%10
            else:
                new_node.val = r
            
            curr.next = new_node
            l1_h = l1_h.next
            l2_h = l2_h.next
            curr = curr.next
        
        while l1_h:
            new_node= ListNode()
            r = l1_h.val + c
            c=0
            if r >= 10:
                c = r//10
                new_node.val = r%10
            else:
                new_node.val = r
            
            curr.next = new_node
            l1_h = l1_h.next
            curr = curr.next
        
        while l2_h:
            new_node= ListNode()
            r = l2_h.val + c
            c=0
            if r >= 10:
                c = r//10
                new_node.val = r%10
            else:
                new_node.val = r
            
            curr.next = new_node
            l2_h = l2_h.next
            curr = curr.next
            
        if c>0:
            new_node = ListNode()
            new_node.val = c 
            curr.next = new_node

        l3=l3.next
        return l3
        
def to_linked_list(input)->ListNode:
    l = ListNode
    curr = l 
    for n in reversed(input):
        new_node = ListNode(int(n),None)
        curr.next = new_node
        curr = curr.next
    l=l.next
    return l

def print_linked_list(node:ListNode):
    while node:
        print(node.val)
        node = node.next
        
# n1 = to_linked_list("123")
# n2 = to_linked_list("456")
# print_linked_list(Solution().addTwoNumbers(n1,n2))
# n1 = to_linked_list("999")
# n2 = to_linked_list("1")
# print_linked_list(Solution().addTwoNumbers(n1,n2))
n1 = to_linked_list("567")
n2 = to_linked_list("56")
print_linked_list(Solution().addTwoNumbers(n1,n2))