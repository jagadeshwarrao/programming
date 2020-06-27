# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if head:
        if position == 0:
            head = head.next
        else:
            previous = None
            current = head
            current_position = 0
            while (current_position < position) and (current.next is not None):
                previous = current
                current = current.next
                current_position += 1
            previous.next = current.next
    return head


def delete_recursive(head, position):
    if position == 0:
        return head.next
    else:
        head.next = delete_recursive(head.next, position - 1)
        return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()
