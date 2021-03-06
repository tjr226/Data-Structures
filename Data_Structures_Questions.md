Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1-3 are all constant 

1. What is the runtime complexity of `enqueue`?

2. What is the runtime complexity of `dequeue`?

3. What is the runtime complexity of `len`?

## Binary Search Tree

all are O(log n)
this assumes that, on average, the tree is balanced

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

## Heap

1. What is the runtime complexity of `_bubble_up`?

log n

2. What is the runtime complexity of `_sift_down`?

log n

3. What is the runtime complexity of `insert`?

log n

4. What is the runtime complexity of `delete`?

log n

5. What is the runtime complexity of `get_max`?

constant

## Doubly Linked List

1-10 are all constant time

10a - Delete is constant, JS array.splice can be linear in the worst case

1. What is the runtime complexity of `ListNode.insert_after`?

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?