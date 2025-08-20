#get an intiger
n = int(input())

#get numbers n times
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

#find max and min
max_num = max(numbers)
min_num = min(numbers)

#output
print("Max:", max_num)
print("Min:", min_num)
