class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move the first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move both pointers together until the first pointer reaches the end
    while first is not None:
        first = first.next
        second = second.next

    # Remove the nth node by skipping over it
    second.next = second.next.next

    return dummy.next

# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage:
# Construct a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
print_linked_list(head)

n = 2
new_head = remove_nth_from_end(head, n)

print("Linked list after removing the {}th node from the end:".format(n))
print_linked_list(new_head)

