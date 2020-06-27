# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#



def print_list_iterative(head):
    if head:
        current = head
        while current:
            print(current.data)
            current = current.next


def printLinkedList(head):
    if head:
        print(head.data)
        printLinkedList(head.next)


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
