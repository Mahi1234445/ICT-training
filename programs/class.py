class class1:
    def __init__(self):
        pass
    id=10
    name="abcd"

class class2(class1):
    add="qwerty"

class class3(class2):
    new="name"

obj= class3()

print(obj.add)
print(obj.id)
