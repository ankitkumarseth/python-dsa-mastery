from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedLists:
    """
    Practice fundamental Linked List algorithms.
    """

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, reverse the list, and return the reversed list.
        """
        curr = head
        prev = None
        while curr is not None: # or while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def has_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Return True if the linked list has a cycle in it.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
