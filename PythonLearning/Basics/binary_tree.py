import math

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Iterative way of solving
def depthFirstValues(root):
    if root == None: return []
    result = []
    stack = [root]

    while len(stack) > 0:
        curr = stack.pop()
        result.append(curr.val)

        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    
    return result

# Recursive way of solving
# def depthFirstValues(root):
#     if root == None: return []
#     leftVal = depthFirstValues(root.left)
#     rightVal = depthFirstValues(root.right)
#     return [root.val, *leftVal, *rightVal]

# # Test case 1
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# print(depthFirstValues(a))

# # Test Case 2
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# #    /
# #   g

# print(depthFirstValues(a))
# #   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']

# # Test Case 3
# a = Node('a')
# #     a
# print(depthFirstValues(a)) 
# #   -> ['a']

# # Test Case 4
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# a.right = b;
# b.left = c;
# c.right = d;
# d.right = e;

# #      a
# #       \
# #        b
# #       /
# #      c
# #       \
# #        d
# #         \
# #          e

# print(depthFirstValues(a)) 
# #   -> ['a', 'b', 'c', 'd', 'e']

# # Test Case 5
# print(depthFirstValues(None)) 
# #   -> []

# Iterative Soultion to the Breath First
# Breath First needs a queue so recusrive uses a stack which doesnt work
def breadthFirstValues(root):
    if root == None: return []
    result = []
    queue = [root]

    while len(queue) > 0:
        curr = queue.pop(0)

        result.append(curr.val)

        if curr.left != None: queue.append(curr.left)
        if curr.right != None: queue.append(curr.right)
    
    return result

# # Test Case 0   
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# print(breadthFirstValues(a))
# #    -> ['a', 'b', 'c', 'd', 'e', 'f']

# # Test Case 1
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# h = Node('h')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# #    /       \
# #   g         h

# print(breadthFirstValues(a))
# #   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# # Test Case 2
# a = Node('a')
# #      a
# print(breadthFirstValues(a))
# #    -> ['a']

# # Test Case 3
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# x = Node('x')

# a.right = b
# b.left = c
# c.left = x
# c.right = d
# d.right = e

# #      a
# #       \
# #        b
# #       /
# #      c
# #    /  \
# #   x    d
# #         \
# #          e

# print(breadthFirstValues(a))
# #    -> ['a', 'b', 'c', 'x', 'd', 'e']

# # Test Case 4
# print(breadthFirstValues(None))
# #    -> []

# Iterative Breath First Version
def tree_includes(root, target):
    if root == None: return False
    queue = [root]

    while len(queue) > 0:
        curr = queue.pop(0)
        if curr.val == target: return True

        if curr.left: queue.append(curr.left)
        if curr.right: queue.append(curr.right)
    
    return False

# Recursive Depth First Version
def treeIncludes(root, target):
    if root == None: return False
    if root.val == target: return True

    return treeIncludes(root.left, target) or treeIncludes(root.right, target)

# # Test Case 0
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# print(tree_includes(a, "e")) # -> True

# # Test Case 1
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# print(tree_includes(a, "a")) # -> True

# # Test Case 2
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# print(tree_includes(a, "n")) # -> False

# # Test Case 3
# print(tree_includes(None, "b")) # -> False

# Recusrsive Depth First Style
# def tree_sum(root):
#     if root == None: return 0
#     return root.val + tree_sum(root.left) + tree_sum(root.right)

# Iterative Breath First Version
def tree_sum(root):
    if root == None: return 0
    queue = [root]
    sum = 0

    while len(queue) > 0:
        curr = queue.pop(0)
        sum += curr.val

        if curr.left != None: queue.append(curr.left)
        if curr.right != None: queue.append(curr.right)
    
    return sum

# # Test Case 0
# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #       3
# #    /    \
# #   11     4
# #  / \      \
# # 4   -2     1

# print(tree_sum(a)) # -> 21

# # Test Case 1
# a = Node(1)
# b = Node(6)
# c = Node(0)
# d = Node(3)
# e = Node(-6)
# f = Node(2)
# g = Node(2)
# h = Node(2)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #      1
# #    /   \
# #   6     0
# #  / \     \
# # 3   -6    2
# #    /       \
# #   2         2

# print(tree_sum(a)) # -> 10

# # Test Case 2
# print(tree_sum(None)) # -> 0

# Iterative Solution
# def tree_min_value(root):
#     smallest = math.inf
#     stack = [root] # can change to queue

#     while len(stack) > 0:
#         curr = stack.pop() # changes to curr = queue.pop(0)
        
#         if curr.val < smallest: smallest = curr.val

#         if curr.left != None: stack.append(curr.left)  # queue.append(curr.left)
#         if curr.right != None: stack.append(curr.right) # queue.append(curr.right)
    
#     return smallest

# Recusrive of Depth First
def tree_min_value(root):
    if root == None: return math.inf
    left_min = tree_min_value(root.left)
    right_min = tree_min_value(root.right)

    return min(root.val, left_min, right_min)

# # Test Case 0
# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #       3
# #    /    \
# #   11     4
# #  / \      \
# # 4   -2     1
# print(tree_min_value(a)) # -> -2

# # Test Case 1
# a = Node(-1)
# b = Node(-6)
# c = Node(-5)
# d = Node(-3)
# e = Node(-4)
# f = Node(-13)
# g = Node(-2)
# h = Node(-2)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #        -1
# #      /   \
# #    -6    -5
# #   /  \     \
# # -3   -4   -13
# #     /       \
# #    -2       -2

# print(tree_min_value(a)) # -> -13

# # Test Case 2
# a = Node(42)
# #        42
# print(tree_min_value(a)) # -> 42

# Recursive Solution
def max_path_sum(root):
    if root == None: return -math.inf
    if root.left == None and root.right == None: return root.val

    the_max = max(max_path_sum(root.left), max_path_sum(root.right))
    return root.val + the_max

# # Test Case 0
# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #       3
# #    /    \
# #   11     4
# #  / \      \
# # 4   -2     1

# print(max_path_sum(a)) # -> 18

# # Test Case 1
# a = Node(5)
# b = Node(11)
# c = Node(54)
# d = Node(20)
# e = Node(15)
# f = Node(1)
# g = Node(3)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# e.left = f
# e.right = g

# #        5
# #     /    \
# #    11    54
# #  /   \      
# # 20   15
# #      / \
# #     1  3

# print(max_path_sum(a)) # -> 59

# # Test Case 2
# a = Node(-1)
# b = Node(-6)
# c = Node(-5)
# d = Node(-3)
# e = Node(0)
# f = Node(-13)
# g = Node(-1)
# h = Node(-2)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #        -1
# #      /   \
# #    -6    -5
# #   /  \     \
# # -3   0    -13
# #     /       \
# #    -1       -2

# print(max_path_sum(a)) # -> -8

# # Test Case 3
# a = Node(42)
# #        42
# print(max_path_sum(a)) # -> 42