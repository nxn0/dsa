# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        c = [0,0]
        mn, i = inf, 1
        pr, cr, nx = head, head.next, head.next.next

        while nx:
            if (cr.val-pr.val)*(cr.val-nx.val) > 0:
                if c[0]: mn = min(mn, i-c[c[1] > 0])
                c[c[0] > 0] = i
            pr , cr,nx = cr, nx, nx.next
            i +=1
        return [[mn, c[1] - c[0]], [-1, -1]][not c[1]]        