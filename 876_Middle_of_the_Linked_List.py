from typing import Any

class Node:
    def __init__(self, data):
        self.data: Any = data
        self.next: None | Node = None 

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes: Any = None):
        self.head: None | Node = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

ll = LinkedList(['1', '2', '3', '4', '5', '6'])

# def mid_ll(head):
#     if head is not None:
#         slow = head.val
#         fast = slow

#         while True:
#             try:
#                 if fast.next is None:
#                     break
#                 fast = fast.next.next
#                 slow = slow.next
#             except AttributeError:
#                 break
#         return slow
#     return None

def mid_ll(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
mid_ll(ll.head)