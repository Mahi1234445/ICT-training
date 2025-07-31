#read n lines
a=int(input("enter"))
with open("myfile.txt","w") as file:
    file.write("hello\nhellooooo\nhello\nhello")

    
with open("myfile.txt","r") as file:
     lines=file.readlines()
     for i in range(a):
         print(lines[i])


#max length 


#number of lines