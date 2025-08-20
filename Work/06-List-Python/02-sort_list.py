#inpt
n = int(input())

#get n number
numbers = []
for _ in range(n):
    num = int(input())
    numbers+=[num]

#print ori list
print("Original list:", numbers)

#sort
numbers.sort()

#print sorted list
print("Sorted list:", numbers)
