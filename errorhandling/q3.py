def file(name):
    try:
        f=open(name,"r")
        a=f.read()
        print(a)
        f.close()
    except FileNotFoundError:
        print("File not found")

n=input("enter file name")
file(n)