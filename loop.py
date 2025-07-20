# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dua dummy node untuk head list "kecil" dan "besar atau sama"
        before_head = ListNode(0)
        after_head = ListNode(0)

        # Pointer saat ini untuk membangun kedua list
        before = before_head
        after = after_head

        # Iterasi melalui list asli
        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next

        # Penting! Akhiri list "after" agar tidak terhubung ke node lama
        after.next = None

        # Gabungkan dua list: before -> after
        before.next = after_head.next

        return before_head.next
