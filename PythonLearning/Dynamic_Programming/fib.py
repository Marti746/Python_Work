# Basic function of Fib without really using Dynamic Programming
# def fib (n):
#     if n <= 2: return 1
#     return fib(n - 1) + fib(n -2)

# print(fib(6)) # 8
# print(fib(7)) # 13
# print(fib(8)) # 21
# print(fib(50)) # takes a while to print out

# memoization
# Store duplicate sub problems (HashMap equivalent)
# python object keys will be arg to fn: value will be return value
def fib (n, memo = {}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fib(n - 1, memo) + fib(n -2, memo)
    return memo[n]

print(fib(6)) # 8
print(fib(7)) # 13
print(fib(8)) # 21
print(fib(50)) # prints faster