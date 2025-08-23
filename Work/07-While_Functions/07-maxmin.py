import math

s=input()
mx=-math.inf
mn=math.inf

while(s!='end'):
    n=float(s)
    mx=max(mx, n)
    mn=min(mn, n)
    s=input()

if(mx==-math.inf and mn==math.inf): print("No data")
else: 
    print ("Max value: ", mx)
    print ("Min value: ", mn)