# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        # we have found the middle
        # build the second array by 


        prev = None
        curr = slow.next 
        slow.next = None

        # reverse

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # merge

        first = head
        second = prev

        # 1 2
        # 3 4 5
        # alternate them
        
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

            
                




        






            
        