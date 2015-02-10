#Aunik Hussain
#Files Revision Exercise 1
#10/02/2015

with open("revex1.txt",mode="a",encoding="utf-8") as my_file:
    for count in range(5):
        name = input("please enter some text")
        my_file.write(name+"\n")
    
