# def howSum(targetSum, numbers):
#     if targetSum == 0: return []
#     if targetSum < 0: return None

#     for num in numbers:
#         remainder = targetSum - num
#         results = howSum(remainder, numbers)
#         if results != None: return [*results, num] # spread operator
    
#     return None

# m = target sum
# n = numbers length
# Brute Force
# time: O(n^m * m)
# space: O(m)

def howSum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        remainder = targetSum - num
        results = howSum(remainder, numbers, memo)
        if results != None: 
            memo[targetSum] = [*results, num] # spread operator
            return memo[targetSum]
    
    memo[targetSum] = None
    return None

print(howSum(7, [2,3])) # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7])) # [4, 3]
print(howSum(7, [2, 4])) # null/none
print(howSum(8, [2, 3, 5])) # [2, 2, 2, 2]
print(howSum(300, [7, 14])) # null/none
