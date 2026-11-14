#simrin didnt join 14.11.2026

#maximum sum of subarray

number = [2,1,5,1,3,2]

k = 3

maximum = 0

for i in range(len(number)-k+1):
    total = 0 
    for j in range(i, i+k):
        total +=number[j]
    if total > maximum:
        maximum = total

print("maximum sum:", maximum)