class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Iterative way of solving
# def depthFirstValues(root):
#     if root == None: return []
#     result = []
#     stack = [root]

#     while len(stack) > 0:
#         curr = stack.pop()
#         result.append(curr.val)

#         if curr.right: stack.append(curr.right)
#         if curr.left: stack.append(curr.left)
    
#     return result

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

# Test Case 0   
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(breadthFirstValues(a))
#    -> ['a', 'b', 'c', 'd', 'e', 'f']

# Test Case 1
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

print(breadthFirstValues(a))
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Test Case 2
a = Node('a')
#      a
print(breadthFirstValues(a))
#    -> ['a']

# Test Case 3
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
x = Node('x')

a.right = b
b.left = c
c.left = x
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#    /  \
#   x    d
#         \
#          e

print(breadthFirstValues(a))
#    -> ['a', 'b', 'c', 'x', 'd', 'e']

# Test Case 4
print(breadthFirstValues(None))
#    -> []