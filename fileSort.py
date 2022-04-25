import os
import os.path
import shutil


#
# Classifies the files
#

def classify_files(path, L) :
    '''' Checks each file for key words to classify the file
    '''

    d = {}
    for key in L:
        d[key] = []
    
    
    AllFiles = list(os.walk(path))
    # print(AllFiles)    

    for item in AllFiles:
        foldername, LoDirs, LoFiles = item   # cool unpacking!
        
        for filename in LoFiles:
                if filename[-3:] == "txt":
                    fullfilename = foldername + "/" + filename
                    # print(fullfilename)
                    f = open(fullfilename, "r", encoding="latin1")
                    contents = f.read()
                    for grade in d:
                        if grade in contents:
                            d[grade].append(fullfilename) 
                    f.close()
    return d


# 
# Makes new directories to store the different categories
# 

def make_directories(dictionary) :
    ''' Makes new directories to store the different categories
    '''
    currentdir = os.getcwd()
    # print(currentdir)

    LoNewDir = []
    joinedDir = []

    for key in dictionary:
        LoNewDir.append(key)

    for newdir in LoNewDir:
        if not os.path.exists(newdir):
            joinedDir.append(os.path.join(currentdir, newdir))
        
    print(f"joinedDir is {joinedDir}")


#
# Copies the recipes into their corresponding folder
# 

def copy_files(dictionary) :
    ''' Moves copies of each recipe into its correct folder
    '''
    for category in dictionary :
        print(f"category: {category} \n")
        for file in dictionary[category]:
            print(f"file: {file} \n")
            try:
                slicePlace = file.index("/")
                filename = file[slicePlace+1:]
                filedirec = file[:slicePlace]

                print(f"filename: {filename} \n")
                print(f"filedirec: {filedirec} \n")


                newfilepath = os.path.join(currentdir, category, filename)

                print(f"copying {file}")
                print(f"to {newfilepath} \n")

                if not os.path.exists(newfilepath):
                    shutil.copy(file,newfilepath)

            except FileNotFoundError as e:
                print(f"***   Copying did not work   *** ")
                print(f"Python's error message: {e}") 


def addtoFile(file, name, descript, age, subject, country):
    f = open(file, 'w')
    f.write(f"Name: {name}")
    f.write('\n')
    f.write(f"Description: {descript}")
    f.write('\n')
    f.write(f"Age: {age}")
    f.write('\n')
    f.write(f"Subject: {subject}")
    f.write('\n')
    f.write(f"Country: {country}")
    f.write('\n')
    f.close()



if True:

    # sign on
    print(f"[[ Start! ]]\n")

    currentdir = os.getcwd()
    # countries = ["United States", "Canada"]
    # d = classify_files(currentdir, countries)
    # print(d)
    # print()


    # make_directories(d)
    # print()

    # copy_files(d)

    # addtoFile(currentdir+'/Kindergarten.txt', "hihihi", "hihih", "hihih", "hi", "hihihihi")