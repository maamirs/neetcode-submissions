# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        # traverse to find size of the list


        curr = head

        count = 0

        while curr:
            curr = curr.next
            count += 1


        toremove = count - n
        

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        count = 0
        while curr.next:
            if count == toremove:
                curr.next = curr.next.next
                break
            curr = curr.next
            count += 1

        return dummy.next


# def removeNthFromEnd(self, head, n):
#     dummy = ListNode(0)
#     dummy.next = head

#     fast = dummy
#     slow = dummy

#     # move fast n+1 steps ahead
#     for i in range(n + 1):
#         fast = fast.next

#     # move both until fast hits end
#     while fast:
#         fast = fast.next
#         slow = slow.next

#     # slow is now just before the node to remove
#     slow.next = slow.next.next

#     return dummy.next

