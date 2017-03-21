#!/usr/bin/python3
import os, sys, collections
from os import listdir, sep
from sys import argv
import argparse

# -- Static lists ------------------------------------------------------

blackList = [',', '..', '.DS_Store', '._.DS_Store']

# -- Class / Def -------------------------------------------------------

def findInserts(file):
	result = -1
	hitList = {}
	while 1:
		result = file.find('%', result + 1)
		if result == -1:
			break
		else:
			hitList[result] = int(file[result + 1])
	return collections.OrderedDict(sorted(hitList.items(), reverse=True))


def processFiles(simulate):
        preserved = ''
        for fileName in allFiles:
            if args.preserve:
                    preserved = fileName[preservePos - 1:-4]
            newName = savedNewName
            fName, fExt = os.path.splitext(fileName)
            fSplit = fName.split(delimiter)

            for key in inserts.keys():
                firstPart = newName[:key]
                secondPart = newName[key + 2:]
                middlePart = fSplit[inserts[key]]
                newName = firstPart + middlePart + secondPart
            newName = (newName + preserved).replace(' ', '.') + fExt
            print(fileName, '------->', newName)
            if not simulate:
                    os.rename(fileName, newName)


# -- Main -------------------------------------------------------

if sys.version_info.major < 3:
        print('Please use Python3 to execute this script!')
        sys.exit()
parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=40))
parser.add_argument("-s", "--simulate",     action="store_true", default=False, help="Skips the actual rename")
parser.add_argument("-p", "--preserve",     action="store_true", default=False, help="Preserve a part of the name")
args = parser.parse_args()

baseDir = os.getcwd()
allFiles = []
for file in os.listdir(baseDir):
    if file not in blackList:
        allFiles.append(file)
print('')
print('Directory is "' + baseDir + '":')
print('---------------------------------------------------')
print('First File: ', allFiles[0][:-4])
print('             0    5    0    5    0    5    0    5    0    5    0    5    0    5    0    5    0    5    0')
print('---------------------------------------------------')
print()

if args.preserve:
        preservePos = int(input('   Preserve from what position?: ')) + 1
delimiter = input('Split on what sign?: ')
sentenceSplit = allFiles[0][:-4].split(delimiter)
print(sentenceSplit)
newName = input('   Type new sentence. Use <%1> for adding split parts: ')
inserts = findInserts(newName)
savedNewName = newName

print('')
print('Done analyzing. Working through files...')
print('---------------------------------------------------')

if not args.simulate:
        processFiles(False)
else:
        processFiles(True)
        doProc = input('Simulation completed. Process files (y/n)? : ')
        if doProc == 'y':
                processFiles(False)
                


print('---------------------------------------------------')
print('All Done!')
print()


#       cd C:\MAC_Office2011
#       "c:\Program Files\Python33\python.exe" z:\Python\MassRename.py
#               HerErNrSyv>%7<OgNr>%2<OgIgenNr>%7<











