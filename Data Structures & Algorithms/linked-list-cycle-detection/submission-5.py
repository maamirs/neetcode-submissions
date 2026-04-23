
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # basically have one moving faster than the other
        # 1 2 3 4

        if not head or not head.next:
            return False

        curr = head
        faster = head.next

        while faster and faster.next:
            if curr == faster:
                return True
            
            curr = curr.next
            faster = faster.next.next
            
        
        return False
