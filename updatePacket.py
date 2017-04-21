import os
from shutil import copyfile
from subprocess import call

def ensure_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

def list_files(path):
    # returns a list of names (with extension, without full path) of all files 
    # in folder path
    files = []
    for name in os.listdir(path):
	if name.endswith(".pdf"):
            files.append(name)
    return files 




#directory = os.path.dirname(file_path)

currentDirectory = os.getcwd()

print "Current working directory is" + currentDirectory
if("password" in currentDirectory):
    confirm = raw_input("You are in the password directory, continue? ")
    if( (confirm != "y") or (confirm != "Y")):
        exit()
        
desiredDirectory = currentDirectory + "/password"

ensure_dir(desiredDirectory)

fileList = list_files(currentDirectory)

print "Select file to encrypt"

for each in range(len(fileList)):
	print str(each) + " - " + fileList[each]

selection = raw_input()

fileToCopy = fileList[int(selection)]

print "file selected: " + fileToCopy
extension = raw_input("Please enter the 4 characters for the new file: ")

#Copy the contents of the file named src to a file named dst
src = currentDirectory + "/" + fileToCopy
dst = desiredDirectory + "/" + fileToCopy

dst2 = desiredDirectory + "/" + fileToCopy[0:len(fileToCopy)-4] + "_" + extension +".pdf"


print "Copying file into password folder: "
print "src: " + src
print "dst: " + dst

if os.path.exists(dst):
	confirm = raw_input("destination file already exists, overwrite? (y/n) ")
	if( (confirm == "y") or (confirm == "Y")):
                            copyfile(src, dst)
else:
	copyfile(src, dst)

encryptCommand = "pdftk " + dst + " output " + dst2 + " userpw " 

password = raw_input("Enter the password to encrypt the pdf with: ")

encryptCommand = encryptCommand + password 

print
print encryptCommand
print

os.system(encryptCommand)
