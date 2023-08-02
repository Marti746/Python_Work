# regualr way of calling without Dynamic Programming
# def gridTraveler(m, n):
#     if m == 1 and n == 1: return 1
#     if m == 0 or n == 0: return 0
#     return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)


# print(gridTraveler(1,1)) # 1
# print(gridTraveler(2,3)) # 3
# print(gridTraveler(3,2)) # 3
# print(gridTraveler(3,3)) # 6
#print(gridTraveler(18,18)) # 2333606220 prints really slow

# memoization
def gridTraveler(m, n, memo={}):
    # checks are the arg in the memo
    key = str(m) + ',' + str(n)

    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0

    memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[key]

print(gridTraveler(1,1)) # 1
print(gridTraveler(2,3)) # 3
print(gridTraveler(3,2)) # 3
print(gridTraveler(3,3)) # 6
print(gridTraveler(18,18)) # 2333606220 prints faster