class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        # Swapping nodes
        prev.next = second
        first.next = second.next
        second.next = first

        # Move to the next pair
        prev = first

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

new_head = swap_pairs(head)

print("Linked list after swapping every two adjacent nodes:")
print_linked_list(new_head)

