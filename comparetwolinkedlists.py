# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(headA, headB):
    if headA is None or headB is None:
        return 0
    else:
        nodeA = headA
        nodeB = headB
        flag = 0 
        while nodeA is not None and nodeB is not None:
            if nodeA.data != nodeB.data:
                flag = 2
            nodeA= nodeA.next
            nodeB=nodeB.next
        if flag == 2:
            return 0
        else:
            if nodeA is None and nodeB is not None:
                return 0
            elif nodeB is None and nodeA is not None:
                return 0
            else:
                return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
