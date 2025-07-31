with open ("myfile.txt","r") as file:
    a=file.readlines()
    print(max(a))