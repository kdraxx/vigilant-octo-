def isprime(num):
    fc=0
    for i in range(1,num+1):
        if num%i==0:
            fc+=1
    return fc==2
sum=0
for i in range(1,2000000):
    if i%2==0 or i%3==0 or i%5==0 or i%7==0 :
        continue
    elif isprime(i):
        sum+=i
print(sum)

