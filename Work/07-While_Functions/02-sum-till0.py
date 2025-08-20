def ad(a):
    global sum
    sum+=a

sum=x=int(input())

while(x!=0):
    x=int(input())
    ad(x)


print("Sum: ", sum)