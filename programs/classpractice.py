'''import array
for name in array.__dict__:
    print(name)
'''
class parent:
    a=10
class child(parent):
    b=15
class chlid_child(child):
    def sum(self):
        print(self.a+self.b)
obj=chlid_child()
obj.sum()
