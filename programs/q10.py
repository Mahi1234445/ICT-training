#perfect number
n=int(input("Enter number to check if it is a perfect number"))
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)

sum=sum(l)

if sum==n:
    print("number is perfect")
else:
    print("number is not perfect")



