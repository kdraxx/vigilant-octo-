import math
i=11
while True:
    sum=0
    x=str(i)
    for j in x:
        z=int(j)
        y=math.factorial(z)
        sum+=y
        if sum==int(x):
            print(i)
            sum=0
    i+=1