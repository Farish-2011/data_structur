# simrin didnt join 14.11.2026
#reaverse an array two pointers and withouth using bullt-in functions or slicing
#ager sillebus e ferot gese
numders = [10,20,30,40,50]

left = 0
right = len(numders) - 1 

while left < right:
    temp = numders[left]
    numders[left] = numders[right]
    numders[right] = temp

    left +=1
    right -=1

print("reversed array: ",numders)