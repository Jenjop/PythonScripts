import os,re

nameRegex = re.compile(r'''
    (.*)    #Name of file --> Group 1
    \.      #Period
    nomedia     #Extension
    ''',re.VERBOSE) ##Use re.VERBOSE to allow with ''' to allow regex to span multiple lines

            
for filename in os.listdir():
    if filename.endswith("nomedia"):
        nameSearch = nameRegex.search(filename)
        file = nameSearch.group(1)
        os.rename(filename,file)
        print (file)
##        command = input()
##        if ("1" in command.lower() or '1' in command):
##            os.rename(filename,file)
##        print (file)
##    print (filename)
