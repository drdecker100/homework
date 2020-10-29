#All you need to do was to change p to path to match the variable. 
#  https://www.w3schools.com/python/python_functions.asp
import os

#create a function that takes two arguments/parameters, the path and the indent
#the path is where you want to a file or directory is located
#the indent is used in the print function in the code for spacing of the output

#listdir() method in python is used to get the list of all files and directories in the specified directory. 
#If we don't specify any directory, then list of files and directories in the current working directory will be returned.

#we use if statement to control the flow
#in the first if block, when the expresion is true, the code is executed
#if the expression is false, we skip to the next elif statement

# the first expression states that if the content of the path inputted is a file,then we indent the items and print them
#the second expression says that if the content of the path is a folder, label them red and print the items

#the function is called again to list out the content of the folder

def process_dir(path, indent):   
    for item in os.listdir(path):   
        if os.path.isfile("{0}/{1}".format(path, item)):
            print("\t"*indent, item)           
        elif os.path.isdir("{0}/{1}".format(path, item)):
            print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))
            
            process_dir("{0}/{1}".format(path, item), indent+1)
        else:
            print("Not a file or directory")


path=input("Enter a valid system path: ")
print("\x1b[1;31m{}\x1b[0;0m".format(path))
process_dir(path, 1)
