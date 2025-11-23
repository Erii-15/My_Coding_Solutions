# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        current=head
        prev=None

        seen=set()
        while current:
            if current.val not in seen:
                seen.add(current.val)
                prev=current
            else:
                prev.next = current.next
            
            current=current.next
        return head   