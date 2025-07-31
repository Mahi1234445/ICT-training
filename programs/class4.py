class parent:
    def display(self,name):
        print(name)

class child(parent):
    def display(self,classn,id,name):
        print(classn,id,name)
class child_child(child):
      def display(self,id):
        print(id)

a=int(input("Enter your choice 1. Name 2. classn ,id, age 3.id"))
if(a==1):
    obj=parent()
    obj.display("mahi")
elif(a==2):
    obj=child()
    obj.display(4,10,"mahi")
elif(a==3):
    obj=child_child()
    obj.display(4)
