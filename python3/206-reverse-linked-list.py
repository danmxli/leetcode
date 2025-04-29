from typing import Optional


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# print function
def print_list(node: Node):
    while node is not None:
        print(node.val)
        node = node.next

# reverse a linked list using a stack
def reverse_list(head: Optional[Node]):
    stack = []

    temp = head
    while temp.next is not None:
        stack.append(temp)
        temp = temp.next
    
    # assign last node as new head
    head = temp
    while (stack):
        ...
        temp.next = stack.pop()
        temp = temp.next
    
    #  terminate the new list
    temp.next = None
    return head

# sample list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# print_list(head)
head = reverse_list(head)
print_list(head)
