# def canSum(targetSum, num):
#     if targetSum == 0: return True
#     if targetSum < 0: return False

#     for n in num:
#         remainder = targetSum - n
#         if canSum(remainder, num) == True:
#             return True
    
#     return False

# Memoization method
def canSum(targetSum, num, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False

    for n in num:
        remainder = targetSum - n
        if canSum(remainder, num, memo) == True:
            memo[targetSum] = True
            return True
    
    memo[targetSum] = False
    return False

print(canSum(7, [2, 3], {})) # true
print(canSum(7, [5, 3, 4, 7], {})) # true
print(canSum(7, [2, 4], {})) # false
print(canSum(8, [2, 3, 5], {})) # true
print(canSum(300, [7, 14], {})) # false
# will output true for all if not sent a empty memo object since the memo object retains past method call info