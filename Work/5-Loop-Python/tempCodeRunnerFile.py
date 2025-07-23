sum=0
n=int(input("enter your number: ")) #get number
for i in range (1, n+1): #loop n times
    if(i%2==0): sum+=i #check wheater its even
    #print (i) testing
print(sum) #output