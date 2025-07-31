def divide(n,d):
    try:
        ans=n/d
        print(ans)
    

    except ZeroDivisionError:
        print("division by 0")
n=100
d=0
divide(n,d)