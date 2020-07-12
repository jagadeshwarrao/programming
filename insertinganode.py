"""
reference data types:

class LLNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""

class Solution:
    def insertNodeAtPosition(self, head, data, position):
        # write your method here
        node = LLNode(data)
        if not head:
            head = node
        elif position == 0:
           
            node.next = head
            head = node
        else:
            previous =LLNode(data)
            current = head
            current_position = 0
            while (current_position < position)  :
                previous = current
                current = current.next
                current_position =current_position+ 1
            previous.next = node
            node.next = current
        return head
        