'''primesum=0
for i in range(1,2000000):
    fc=0
    for j in range(1,i):
        if i%j==0:
            fc+=1
        if fc==2:
            primesum+=i
print(primesum)'''
s=2
for i in range (3,2000000):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        s+=i

print(s)

