#generate random nummber
start=int(input("enter start"))
end=int(input("enter end"))
import random
def generate(start,end):
    for i in range(start,end+1):
        yield random.randint(start,end)
a=generate(start,end)
for j in range (10):
    print(next(a))