def isprime(num):
    fc=0
    for i in range(1,num+1):
        if num%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False
l=[]
fac=0
num= int(input("Enter any number:"))
for i in range(1,num+1):
    if num%i==0:
        fac+=1
        if isprime(i):
            l.append(i)
print(l)

