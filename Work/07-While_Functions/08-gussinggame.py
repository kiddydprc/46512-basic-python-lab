import random
secret=random.randint(1,20)


tries=1
ges=int(input())

while(ges!=secret):
    if(ges<secret): print("too low!")
    else: print("too much!")
    ges=int(input())
    tries+=1


print("Correct! You guess", tries, "time(s)")