import pytest
from src.linked_lists import LinkedLists, ListNode

class TestLinkedLists:
    
    def setup_method(self):
        self.sol = LinkedLists()

    def list_to_array(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr

    def array_to_list(self, arr):
        if not arr: return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def test_reverse_list(self):
        head = self.array_to_list([1, 2, 3, 4, 5])
        rev = self.sol.reverse_list(head)
        assert self.list_to_array(rev) == [5, 4, 3, 2, 1]

        head2 = self.array_to_list([1, 2])
        rev2 = self.sol.reverse_list(head2)
        assert self.list_to_array(rev2) == [2, 1]

        assert self.sol.reverse_list(None) == None

    def test_has_cycle(self):
        node1 = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2  # Cycle here
        
        assert self.sol.has_cycle(node1) == True

        n1 = ListNode(1)
        n2 = ListNode(2)
        n1.next = n2
        assert self.sol.has_cycle(n1) == False
