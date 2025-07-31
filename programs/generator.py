def asdf(a):
    i=0
    while i<=a:
        yield i
        i+=1
for i in asdf(5):
    print(i)