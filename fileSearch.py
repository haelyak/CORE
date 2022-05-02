import os
import os.path
import shutil

# path = os.getcwd()
def keyword_search(path, keyword) :
    '''' Checks each file for keywords
    '''
    keywordList = []
    AllFiles = list(os.walk(path))
    # print(AllFiles)    

    for item in AllFiles:
        foldername, LoDirs, LoFiles = item   # cool unpacking!
        
        for filename in LoFiles:
                fullfilename = foldername + "/" + filename
                # print(fullfilename)
                f = open(fullfilename, "r", encoding="latin1")
                contents = f.read()
                if keyword in contents:
                    keywordList.append(fullfilename)
                f.close()
    return keywordList



def fileInfo(keywordList):
    fileStuff = {}
    for result in keywordList :
        f = open(result, "r", encoding="latin1")
        contents = f.read()
        slicePlace = result.index("/")
        slicePeriod = result.index(".")
        name = result[slicePlace+1:]
        if name not in fileStuff:
            fileStuff[name] = contents[:-1]
        f.close()
    return fileStuff


def refineSearch(keywordList, keyword):
    refinedList = []
    for result in keywordList :
        f = open(result, "r", encoding="latin1")
        contents = f.read()
        if keyword in contents:
            refinedList.append(result)
        f.close()
    return refinedList



# if True:

#     # sign on
#     print(f"[[ Start! ]]\n")

#     # currentdir = os.getcwd()
#     print(keyword_search('static', "Climate"))

#     print(fileInfo(keyword_search('static', "Climate")))
