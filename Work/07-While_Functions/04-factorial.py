def fac():
    global n
    ans=n
    i=1

    while(i<n):
        ans*=(n-i)
        i+=1

    if(n!=0): print(ans)
    else: print(1)

n=int(input())
fac()