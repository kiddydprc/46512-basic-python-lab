#get an intiger
n = int(input())

#Get numbers and seperate in to two list
even = []
odd = []
for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

#output
print("Even:", even)
print("Odd:", odd)
