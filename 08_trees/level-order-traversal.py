# Binary Tree Level Order Traversal
# LeetCode 102 - Medium
#
# Problem:
#   Given the root of a binary tree, return the level order traversal
#   of its nodes' values (i.e., left to right, level by level).
#
# Clarifications:
#   - Values can be positive or negative
#   - If the tree is empty, return an empty array
#   - If only the root exists, return [[root.val]]
#
# Example:
#
#       3
#      / \
#     9  20
#        / \
#       15   7
#
# Output: [[3], [9, 20], [15, 7]]
#
# Brute Force:
#   DFS (recursion) tracking depth. Not natural for level-by-level output.
#   Time: O(n) | Space: O(n)
#
# Optimised (BFS with queue):
#   Use a queue (deque) for breadth-first search.
#
#   Key insight:
#   At the start of each level, all nodes in the queue belong to that level.
#   Capture len(queue) and loop exactly that many times to process one full level.
#   Push children during the loop — they form the next level.
#
#   Per iteration of the while loop:
#     1. Snapshot the queue length (= number of nodes at this level)
#     2. Pop each node, collect its value into a level list
#     3. Push left and right children if they exist
#     4. Append the completed level list to output
#
# Time: O(n)   — every node visited exactly once
# Space: O(n)  — queue holds at most one full level (up to n/2 nodes in a complete tree)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: TreeNode) -> list[list[int]]:
    output: list[list[int]] = []

    if root is None:
        return output

    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        output.append(level)

    return output

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(level_order_traversal(root))   # expect [[3], [9, 20], [15, 7]]
    print(level_order_traversal(None))   # expect []
    print(level_order_traversal(TreeNode(1)))  # expect [[1]]
