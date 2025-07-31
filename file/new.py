#read write update delete
'''
access modifier
r,w,a
r+, w+, a+
rb wb ab
rb+ wb+ ab+

x - create a file
ninary file .bin+ .dll libary fie woth totally binary data only
read 
readline one line at a time
readlines
'''

'''
with open("myfile.txt","w") as file:
    file.write("hello")
with open ("myfile.txt","r") as file:
    content=file.readlines()
    print(type(content))
'''

'''
Exception Handling:


reading warning at runtime is called exception
warning can be handeled at compile time
(run time pe breaks create karne wala is error warning comes at compile time)

    try:catches error i.e fall back and go to previous state, error state stopped
    except: call back
    finally:runs always wether or ot an error occurs
    raise:can be done at all three states above
    assert:
if an errror arises the state goes to error state which we created because if it goes to intial state again it will get stuck into a loop
name error arises when we use a keyword to name a variable
'''
