import sys 
from os import path, listdir, mkdir, environ
from shutil import which

# Simple copy function
def copy(filepath, to):
    fin = open(filepath, "r", encoding="utf-8")
    fout = open(to, "w", encoding="utf-8")
    # Debug features
    print(fin)
    print(fout)
    for line in fin:
        fout.write(line)
    fin.close()
    fout.close()

# Check if config folder exists and if directory doesn't exist, creates a new one in home folder
def checkConfigFolder():
    home = environ["HOME"]
    if not path.exists(home + "/.config"):
        print(".config folder doesn't exist!")
        print("creating a new one...")
        mkdir(home + "/.config")
        print("ok")
    else:
        print(".config folder exists!")

# Returns position of a .config folder 
def configFolderPosition():
    for v in listdir("."):
        if v == ".config":
            return "./config/"
    path = "../"
    while True:
        for v in listdir(path):
            if v == ".config":
                return path + ".config/"
        path += "../"

# Checks if directory exists in .config and if directory doesn't exist, creates a new one
def checkDir(directories):
    for dir in directories:
        print(dir)
        if not path.exists(configFolderPosition() + dir):
            print("This dir does not exist!")
            answer = input("Create a new dir? y or n\n")
            if answer == "y":
               print("Creating a new one...")
               mkdir(configFolderPosition() + dir)
               print("ok")
            else:
               continue
        else:
            print("This dir exists!")

def scanDirectory(exclude=None):
    # Variable for final data
    data = []
    # Variable for directories
    directories = []
    # Files in dotfiles directory
    for fin in listdir():
        # if file is directory and not member of exclude list
        if path.isdir(fin) and fin not in exclude:
            # if directory name is name of app 
            if which(fin):
                directories += [fin]
                # Variable folders [directory]
                folders = [fin]
                # Check folder
                for folder in folders:
                    for file in listdir(folder):
                        position = folder+"/"+file
                        # if variable file is file then add to the variable data a position of the file
                        if path.isfile(position):
                            data += [position]
                        # if variable file is directory then add to the variable folders a position of the directory
                        elif path.isdir(position):
                            folders += [position]
                            directories += [position]
    return data, directories

print("""
            _________           _________________      _____________
           /   ____  \         /  ___________    /    /___    _____/
          /  /     \  \       /  /           /  /        /   /
         /  /       \  \     /  /           /  /        /   /
        /  /         \  \   /  /           /  /        /   /
       /  /          /  /  /  /           /  /        /   /
      /  /          /  /  /  /           /  /        /   /
     /  /          /  /  /  /           /  /        /   /
    /  /__________/  /  /  /___________/  /        /   /
   /________________/  /________________ /        /__ /        
                                                         files 
                                                          by quant0x2
""")
if sys.platform == "darwin":
    print("Hello macOS!")
elif sys.platform == "linux":
    print("Hello Tux!")
checkConfigFolder()
exclude = [".git","chrome", "gtk", "emacs.d"]
files, paths = scanDirectory(exclude)
checkDir(paths)
for f in files:
    copy(f, configFolderPosition() + f)