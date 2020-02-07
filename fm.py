import io 
import os

home = "C:"
current_dir = home 
stack = []
stack.append(current_dir)

def print_dir(current_dir):
    entries = os.listdir(current_dir)
    for i in range (len(entries)):
        print(i + 1, '. ', entries[i], sep='')
    return entries

def parent_dir(current_dir):
    stack.pop()
    current_dir = stack[len(stack) - 1]
    return current_dir

entries = print_dir(home + '/')

while (True):
    print("Hello! This is a file manager")
    print("Please, enter the number of file or directory:")
    print("If you want to return to your parent directory, press q")
    selection = input()
    if (selection == 'q'):
        current_dir = parent_dir(current_dir)
        entries = print_dir(current_dir)
    else:
        temp = current_dir + '/' + entries[int(selection) - 1]
        current_dir = temp
        stack.append(temp)
        
        if (os.path.isdir(current_dir)):
            print("Your current location is",entries[int(selection) - 1])
            print("You have the following options:")
            print("Press a to rename the directory")
            print("Press b to print number of files in it")
            print("Press c to print number of directories in it")
            print("Press d to list content of the directory")
            print("Press e to add file to this directory")
            print("Press f to add new directory to this directory")
            option_dir=input()

            if (option_dir=='a'):
                print("Please, write a new name for directory")
                newname=input()
                path=current_dir.rsplit("/")
                path.pop()
                newname="/".join(path)+"/"+newname
                os.rename(current_dir,newname)

            elif (option_dir=='b'):
                print(len([iq for iq in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, iq))]))

            elif (option_dir=='c'):
                print(len([iq for iq in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, iq))]))

            elif (option_dir=='d'):
                entries = print_dir(current_dir)

            elif (option_dir=='e'):
                print("Write a name of new file with extension")
                new_file=input()
                newfile=open(current_dir+'/'+new_file, 'w')
                newfile.close()

            elif (option_dir=='f'):
                print("Write a name of new directory")
                new_dir=input()
                os.mkdir(current_dir+'/'+new_dir+'/')

        else:
            print("Your current file is",entries[int(selection) - 1])
            print("You have the following options:")
            print("Press a to rename file")
            print("Press b to add content to this file")
            print("Press c to rewrite content of this file")
            print("Press d to delete file")
            option_file=input()
            if (option_file=='a'):
                print("Please, write a new name for file with extension")
                new=input()
                path=current_dir.rsplit("/")
                path.pop()
                new="/".join(path)+"/"+new
                os.rename(current_dir,new)
            elif (option_file=='b'):
                myFile=open(current_dir, 'a')
                print("please, add content")
                myFile.write(input())
                print("Content was successfully added")
                myFile.close()
            elif (option_file=='c'):
                myFile=open(current_dir, 'w')
                print("Please, rewrite content")
                myFile.write(input())
                print("Content was successfully rewritten")
                myFile.close()
            elif (option_file=='d'):
                print("Are you sure to delete this file?")
                os.remove(current_dir)
                print("FIle was deleted")
            

            

           


            





         