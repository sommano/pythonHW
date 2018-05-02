
def sum_of_initial_odds(nums):
    sum = 0
    for i in nums:
        if i % 2 != 0:
            sum = i + sum
        elif i % 2 ==0:
            return sum
    return sum

nums = [1,3,1,3,2]
print(sum_of_initial_odds(nums))
