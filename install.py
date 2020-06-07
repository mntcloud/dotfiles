import sys 
from os import path, listdir, mkdir
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

# Returns position of a .config folder 
def configPosition():
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
def isDirExist(directories):
    for dir in directories:
        print(dir)
        if not path.exists(configPosition() + dir):
            print("This dir does not exist!")
            answer = input("Create a new dir? y or n\n")
            if answer == "y":
               print("Creating a new one...")
               mkdir(configPosition() + dir)
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
#checkpaths = [".config", ".config/nvim", ".config/fish", ".config/fish/functions"]
# check platform
if sys.platform == "darwin":
    #paths = ["nvim/init.vim", "fish/fish_prompt.fish"]
    #topaths = [checkpaths[1]+"/init.vim", checkpaths[3]+"/fish_prompt.fish"]
    #print("Hello macOS!")
    #print("Installing fish_prompt.fish and init.vim...")
    #print("Checking directories...")
    #isDirExist(checkpaths)
    #print("Copying files...")
    #for i in range(len(paths)):
    #    copy(paths[i], dirPosition() + topaths[i])
    #print("ok")
    exclude = [".git","chrome", "gtk", "emacs.d"]
    files, paths = scanDirectory(exclude)
    isDirExist(paths)
    for f in files:
        copy(f, configPosition() + f)
elif sys.platform == "linux":
    print("Hello Tux!")