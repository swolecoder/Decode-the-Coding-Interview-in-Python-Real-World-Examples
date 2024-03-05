# Definition for singly-linked list.
from ast import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        while len(lists) > 1:
            merge = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 <len(lists) else None

                merge.append(self.merge(l1,l2))
            lists = merge
        return lists[0]


    def merge(self, l1,l2):
        l3 = ListNode(-1)
        l4 = l3


        while l1 and l2:
            if l1.val < l2.val:
                l3.next = ListNode(l1.val)
                l3 = l3.next 
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next 
                l3 = l3.next
        
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return l4.next
        