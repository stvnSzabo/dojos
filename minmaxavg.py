numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

i = 1
max = -999999999999
while i < len(numbers):
    if numbers[i] > max:
        max = numbers[i]
    i += 1
print("max:", max)






numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

i = 1
min = 999999999999
while i < len(numbers):
    if numbers[i] < min:
        min = numbers[i]
    i += 1
print("min:", min)


sum = 0
for k in numbers:
    sum += k
    
avg = sum / (len(numbers))
print("avg: ",avg)