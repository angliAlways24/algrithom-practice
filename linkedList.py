class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

a = [2,3,4,5,6]

head = LinkedListNode(0)
current = head
for i in a:
    tmp = LinkedListNode(i)
    current.next = tmp
    current = current.next


current = head
while current != None:
    print(current.value)
    current = current.next

def findIthNode(i, head):
    if head is None or i <0:
        return None
    if hasCircle(head):
        return None

    current=head.next
    for c in xrange(i):
        if current is not None:
            current=current.next
    return current


def hasCircle(head):
    if head is None:
        return False
    
    slow=head
    fast=head

    while fast is not None:
        slow=slow.next
        fast=fast.next
        if fast is None:
            return False
        fast=fast.next
        if slow==fast:
            return True
    return False



    def flipLinkedList(head):
        if head is None:
            return None
        
        stack=Stack()
        start=head
        while start is not None:
            stack.push(start)
            start=start.next

        newHead = LinkedListNode(0)
        current = newHead
        
        while current is not None:
            tmp = stack.pop()
            current.next = tmp
            current = current.next
        
        result = newHead.next
        newHead.next = None
        return result


def flipLinkedList2(head):
    if head is None:
        return
    
    newhead=None
    oldhead=head

    while oldhead is not None:
        P=oldhead.next
        oldhead.next=newhead
        newhead=oldhead
        oldhead=P
    
    return newhead

def findInjection(head):
    if head is None:
        return None
        
    slow=head
    fast=head

    while fast is not None:
        slow=slow.next
        fast=fast.next
        if fast is None:
            break
        fast=fast.next

        if fast == slow:
            break
    else:
        return None

    fast = head

    while fast != slow:
        fast = fast.next
        slow = slow.next

    return fast