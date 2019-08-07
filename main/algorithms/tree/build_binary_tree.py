'''
Reference: LeetCode #105 and #106
Topic: Using preorder/postorder traversal and inorder traveresal to
       reconstruct a binary tree.
Assumption: All the orders are given in list format.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# preorder and inorder
# First, let's use recursion.
def build_tree_recursive(preorder, inorder):
    if not preorder or not inorder:
        return None

    # First element of preorder gives us the root node val.
    root = TreeNode(preorder[0])

    # Find the position of our root in inorder.
    pivot = inorder.index(root.val)

    # Now, we divide and conquer.
    # For left sub-tree, we know all the nodes will be left to the pivot
    # in inorder. And for preorder, all the left sub-tree nodes will be
    # before right sub-tree.
    left_preorder = preorder[1:pivot + 1]
    left_inorder = inorder[:pivot]
    root.left = build_tree_recursive(left_preorder, left_inorder)

    # For right sub-tree, similar.
    right_preorder = preorder[pivot + 1:]
    right_inorder = inorder[pivot + 1:]
    root.right = build_tree_recursive(right_preorder, right_inorder)

    return root


# Next, a more efficient iterative solution
# Idea for this method is that, inorder will first go to the leftmost
# node, so will preorder. So we keep all the nodes in a stack, if the
# next node in preorder is left child of the last node, simply add it
# stack. If we run out of left children, then we need to go back to
# last parent and add its right child.


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    stack = [root]

    # Start from the first element of the inorder, which is the leftmost element in tree.
    in_idx = 0

    # Traverse all the nodes in preorder.
    for i in range(1, len(preorder)):
        node = TreeNode(preorder[i])
        # Previous node.
        prev = None

        # If stack is not empty and last node in stack equals to current inorder node.
        while stack and stack[-1].val == inorder[in_idx]:
            prev = stack.pop()
            in_idx += 1

        if prev:
            prev.right = node
        else:
            stack[-1].left = node

        # Add the node to stack.
        stack.append(node)

    return root
