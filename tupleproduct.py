def multiple_tuple(nums):
    temp = list(nums)
    product = 1
    for x in temp:
        product *= x
    return product

nums = (4,3,2,2, -1, 18)
print("Original tuple: ")
print(nums)
print('product - multiplying all the numbers of the said tuple:', multiple_tuple(nums))

nums = (2,4,8,8,3,2,9)
print("original tuple: ")
print(nums)
print("product - multiplying all the numbers of said tuple: ",multiple_tuple(nums))