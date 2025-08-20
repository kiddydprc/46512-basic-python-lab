# get an intiger
n = int(input())

#get numbers and seperate number that are in rage 10-50
in_range = []
for _ in range(n):
    num = int(input())
    if 10 <= num <= 50:
        in_range.append(num)

# print number in the range
print("Numbers that're in the range 10-50:", in_range)
