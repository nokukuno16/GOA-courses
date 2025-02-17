def numbers_sum(nums):
    result = 0
    for i in range(len(str(nums))):
        result += int(str(nums)[i])
    print(result)

numbers_sum(232)