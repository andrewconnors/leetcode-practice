class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


def check_for_cycle(head):
    if head is None:
        return False
    
    slow_pointer = head
    fast_pointer = head.next

    while fast_pointer != None and fast_pointer.next != None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True
    
    return False

if __name__=="__main__":
    head = LinkedListNode(2)
    node1 = LinkedListNode(3)
    node2 = LinkedListNode(4)
    node3 = LinkedListNode(5)

    head.next = node1
    node1.next = node2
    node2.next = node3

    print(check_for_cycle(head))