from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    data: list
    next: Any = None

@dataclass
class LinkedList:
    nodes: Any = None
    head: Node | None  = None

    if nodes is not None:
        node = Node(data=nodes.pop(0))
        head = node
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

ll = LinkedList(nodes=['a', 'b'])
ll
for node in ll:
    print(node)