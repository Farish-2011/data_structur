nums = [12, 45, 7, 89, 23, 4]

maximum = nums[0]
minimum = nums[0]

for i in nums:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Maximum number = ", maximum)
print("Minimum number = ", minimum)