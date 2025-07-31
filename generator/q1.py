#cube genrator
n=int(input("Enter a number uptil which you want a cube" ))

def cube(n):
    for i in range(1,n+1):
        yield i**3

for j in cube(n):
    print(j)

