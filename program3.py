number=int(input("Enter any number:"))
square=0
sumofsquare=0
sum=0
squareofsum=0
for i in range(number+1):
    square=i**2
    sumofsquare+=square
    square=0
for i in range(number+1):
    sum+=i
squareofsum=sum**2

print(squareofsum-sumofsquare)