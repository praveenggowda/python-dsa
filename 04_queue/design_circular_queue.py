"""
Problem: Design Circular Queue
LeetCode: 622
Category: Queue
Difficulty: Medium

Problem Statement:
Design your implementation of the circular queue. A circular queue is a linear
data structure that follows FIFO and the last position is connected back to the
first position to form a circle.

Examples:
MyCircularQueue(3)
enQueue(1) -> True       queue: [1]
enQueue(2) -> True       queue: [1, 2]
enQueue(3) -> True       queue: [1, 2, 3]
enQueue(4) -> False      full
Rear()     -> 3
isFull()   -> True
deQueue()  -> True       queue: [2, 3]
enQueue(4) -> True       queue: [2, 3, 4]
Rear()     -> 4

Clarifications:
- 1 <= k <= 1000
- 0 <= value <= 1000
- At most 3000 calls combined

Brute Force:
Use a list with count tracking. enQueue appends, deQueue removes from front.
Time Complexity: O(n) for deQueue (list shift)
Space Complexity: O(k)

Optimized Approach:
Fixed-size array of length k with two pointers: head and tail.
- enQueue: write at tail, advance tail = (tail + 1) % k
- deQueue: advance head = (head + 1) % k
- Rear: read at (tail - 1 + k) % k
- Front: read at head
Use a size counter to distinguish full from empty (both have head == tail).

Complexity:
Time Complexity: O(1) for all operations
Space Complexity: O(k)

Pattern: Array, Queue, Two Pointers
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.head = 0
        self.tail = 0
        self.count = 0
        self.queue = [0] * k

    def enqueue(self, value: int) -> bool:
        if self.count == self.size:
            return False

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count += 1

        return True

    def dequeue(self) -> bool:
        if self.count == 0:
            return False

        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def front(self) -> int:
        if self.count == 0:
            return -1

        return self.queue[self.head]

    def rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.tail - 1 + self.size) % self.size]

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.size


if __name__ == "__main__":
    q = MyCircularQueue(3)
    print(q.enqueue(1))  # True
    print(q.enqueue(2))  # True
    print(q.enqueue(3))  # True
    print(q.enqueue(4))  # False
    print(q.rear())  # 3
    print(q.is_full())  # True
    print(q.dequeue())  # True
    print(q.enqueue(4))  # True
    print(q.rear())  # 4
