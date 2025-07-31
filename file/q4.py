with open("myfile.txt","w") as file:
    file.write("hello")
with open ("myfile.txt","r") as file:
    content=file.readlines()
    print(type(content))