# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def reversePrint(head):
    if head:
        stack = [head]
        while stack[-1].next:
            node = stack[-1]
            stack.append(node.next)
        while stack:
            node = stack.pop()
            print(node.data)


def print_reverse_recursive(head):
    if head:
        reversePrint(head.next)
        print(head.data)

if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)
