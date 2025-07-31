#function lambda generator
def compute(n):
    return lambda x:x*n

result=compute(2)
print("double the number of 20", result(20))







