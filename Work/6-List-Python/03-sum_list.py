#get an intiger
n = int(input())

#get numbers n times
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

#get the sum
total = sum(numbers)

#output
print("Sum:", total)
