l=[]
l2=[]
for i in range(10,1000):
    for var in range(10,1000):
        x=(i*var)
        y=str(x)
        if(y==y[::-1]):
            l.append(y)
for i in l:
    l2.append(int(i))
print(max(l2))