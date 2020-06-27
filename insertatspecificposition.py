#insertnode at specific position

def insertNodeAtPosition(head, data, position):
    n = head
    for _ in range(position - 1):
        n = n.next
        n_next = n.next
    n.next = SinglyLinkedListNode(data)
    n.next.next = n_next
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()