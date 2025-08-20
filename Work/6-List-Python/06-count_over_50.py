#gen an intiger
n = int(input())

#get numbers and count how many numbers>50
count = 0
for _ in range(n):
    num = int(input())
    if num > 50:
        count += 1

#output
print("Number that are above 50:", count)
