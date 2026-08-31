# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first_idx = -1
        prev_idx = -1
        min_dist = float('inf')
        
        prev_node = head
        curr_node = head.next
        idx = 1
        
        while curr_node.next:
            next_node = curr_node.next
            if (curr_node.val > prev_node.val and curr_node.val > next_node.val) or \
               (curr_node.val < prev_node.val and curr_node.val < next_node.val):
                # it's a critical point
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_idx)
                prev_idx = idx
            
            prev_node = curr_node
            curr_node = next_node
            idx += 1
        
        if first_idx == -1 or prev_idx == first_idx:
            return [-1, -1]
        
        max_dist = prev_idx - first_idx
        return [min_dist, max_dist]